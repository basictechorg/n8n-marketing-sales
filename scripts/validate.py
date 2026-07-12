#!/usr/bin/env python3
"""Validate every workflow JSON: parseable, valid node graph, no leaked secrets.
Exit non-zero on any failure. Used by CI and locally.

    python3 scripts/validate.py
"""
import json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'workflows')
SECRET = re.compile(r'sk-[A-Za-z0-9]{20,}|sk-ant-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}'
                    r'|ghp_[0-9A-Za-z]{36}|xox[baprs]-[0-9A-Za-z-]{10,}|AIza[0-9A-Za-z_-]{35}')
ALLOW = re.compile(r'YOUR_|Add your|your-webhook-path|example\.com', re.I)

def check(path):
    errs = []
    raw = open(path, encoding='utf-8', errors='replace').read()
    try:
        d = json.loads(raw)
    except json.JSONDecodeError as e:
        return [f'invalid JSON: {e}']
    nodes = d.get('nodes')
    if not isinstance(nodes, list) or not nodes:
        errs.append('no nodes')
        return errs
    names = [n.get('name', '') for n in nodes]
    if len(names) != len(set(names)):
        errs.append('duplicate node names')
    name_set = set(names)
    for n in nodes:
        t = n.get('type', '')
        if not re.match(r'^(@[\w.-]+/)?[\w-]+\.[\w-]+', t or ''):
            errs.append(f'bad node type: {t!r}')
    conns = d.get('connections', {})
    if isinstance(conns, dict):
        for src, outs in conns.items():
            if src not in name_set:
                errs.append(f'connection from unknown node: {src!r}')
    for m in SECRET.finditer(raw):
        seg = raw[max(0, m.start()-20):m.end()+5]
        if not ALLOW.search(seg):
            errs.append(f'possible secret: {m.group()[:12]}...')
    return errs

def main():
    total = bad = 0
    for dp, dirs, files in os.walk(ROOT):
        for f in files:
            if not f.endswith('.json'):
                continue
            total += 1
            errs = check(os.path.join(dp, f))
            if errs:
                bad += 1
                rel = os.path.relpath(os.path.join(dp, f), os.path.dirname(ROOT))
                print(f'FAIL  {rel}')
                for e in errs:
                    print(f'      - {e}')
    print(f'\n{total - bad}/{total} workflows valid')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
