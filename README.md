<div align="center">

<h1>Marketing, Sales & Growth</h1>

<h3>317 production-ready n8n workflows &mdash; sanitized, modernized, and organized</h3>

<p>
<img alt="Workflows" src="https://img.shields.io/badge/workflows-317-EA4B71?style=for-the-badge">
<img alt="Categories" src="https://img.shields.io/badge/categories-3-0b7f91?style=for-the-badge">
<img alt="License" src="https://img.shields.io/badge/license-MIT-3b82f6?style=for-the-badge">
</p>

<p><em>Marketing, sales, CRM, and analytics automation workflows for n8n.<br>Every workflow is stripped of credentials and secrets, modernized to current n8n nodes and AI models, and validated by CI.</em></p>

</div>

---

## What's inside

| | |
|---|---|
| 🔐 **Clean** | No credentials, secrets, instance IDs, or personal data |
| 🔄 **Current** | Latest AI models (GPT-4o, Claude 4.x, Gemini 2.5) and current n8n nodes |
| ✅ **Validated** | CI checks JSON structure and scans for secrets on every change |
| 📁 **Organized** | Grouped by category for fast browsing |

<p>
<img alt="n8n" src="https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white">
<img alt="OpenAI" src="https://img.shields.io/badge/GPT--4o-412991?style=flat-square&logo=openai&logoColor=white">
<img alt="Claude" src="https://img.shields.io/badge/Claude%204.x-D97757?style=flat-square&logo=anthropic&logoColor=white">
<img alt="Gemini" src="https://img.shields.io/badge/Gemini%202.5-8E75B2?style=flat-square&logo=googlegemini&logoColor=white">
</p>

---

## Categories

| Category | Workflows | Focus |
|---|:--:|---|
| 📣 Content & Marketing &nbsp;·&nbsp; [`content-marketing/`](workflows/content-marketing/) | 158 | SEO, content generation, and publishing pipelines |
| 📈 Sales, CRM & Lead Gen &nbsp;·&nbsp; [`sales-crm-lead-gen/`](workflows/sales-crm-lead-gen/) | 110 | Lead scraping, enrichment, and pipeline automation |
| 📊 Reporting & Analytics &nbsp;·&nbsp; [`reporting-analytics/`](workflows/reporting-analytics/) | 49 | Scheduled reports and KPI digests |

---

## Using a workflow

```text
1.  Open a category folder and pick a .json file
2.  In n8n:  Workflows  →  Import from File
3.  Add your own credentials in each node
    (every slot is labelled  "Add your <service> credential")
4.  Activate
```

> **No secrets in this repo.** Every credential is blanked and labelled — you plug in your own keys inside n8n.

---

## 🔒 Security

Each workflow passes an automated gate on every push:

- **Structure** — valid JSON and a sound node graph
- **Freshness** — no deprecated nodes, no legacy AI models
- **Secrets** — [gitleaks](https://github.com/gitleaks/gitleaks) scan across full history + working tree; secret-scanning and push protection enabled

See [SECURITY.md](SECURITY.md) for the sanitization standard.

## 🙏 Credits

Curated and modernized from the open-source **n8n community** (MIT-licensed). Original authors retain rights to their workflow logic. Source licenses in [THIRD_PARTY_LICENSES/](THIRD_PARTY_LICENSES/); details in [NOTICE](NOTICE).

## 📄 License

[MIT](LICENSE)

<div align="center">
<br><sub>Maintained by <a href="https://github.com/basictechorg">basictechorg</a></sub>
</div>