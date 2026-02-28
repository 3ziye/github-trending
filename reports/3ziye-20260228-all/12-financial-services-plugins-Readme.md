# Claude for Financial Services Plugins

Plugins that turn Claude into a specialist for financial services — investment banking, equity research, private equity, and wealth management. Built for [Claude Cowork](https://claude.com/product/cowork), also compatible with [Claude Code](https://claude.com/product/claude-code).

## Why Plugins

Cowork lets you set the goal and Claude delivers finished, professional work. Plugins let you go further: tell Claude how your firm does analysis, which data sources to pull from, how to handle critical workflows, and what slash commands to expose — so your team gets better and more consistent outcomes.

Each plugin bundles the skills, connectors, slash commands, and sub-agents for a specific financial services workflow. Out of the box, they give Claude a strong starting point for helping anyone in that role. The real power comes when you customize them for your firm — your models, your templates, your processes — so Claude works like it was built for your team.

## What is Claude for Financial Services?

Claude for Financial Services is a comprehensive solution built on Claude for Enterprise with specialized capabilities for financial analysis. It connects Claude to the data sources and tools financial professionals use daily — eliminating the need to juggle multiple browser tabs and improving source verification to reduce the risk of errors from manual data gathering.

## End-to-End Workflows

These plugins aren't just a collection of point tools — they enable complete workflows that span research, analysis, modeling, and output creation:

- **Research to Report**: Pull real-time data from MCP providers, analyze earnings results, and generate publication-ready equity research reports — all in a single session
- **Spreadsheet Analysis**: Build comparable company analyses, DCF models, and LBO models as fully functional Excel workbooks with live formulas, sensitivity tables, and industry-standard formatting
- **Financial Modeling**: Populate 3-statement models from SEC filings, cross-check assumptions against peer data, and stress-test scenarios — with blue/black/green color coding conventions built in
- **Deal Materials**: Draft CIMs, teasers, and process letters, then generate pitch deck slides and strip profiles using your firm's branded PowerPoint templates
- **Portfolio to Presentation**: Screen opportunities, run diligence checklists, build IC memos, and track portfolio KPIs — moving seamlessly from data to deliverable

Each workflow connects upstream data sources (via MCP) to downstream outputs (Excel, PowerPoint, Word), so you move from question to finished work product without context-switching.

## Plugin Marketplace

Start with **financial analysis** — the core plugin that provides shared modeling tools and all MCP data connectors. Then add any function-specific plugins to enhance Claude's capabilities for your workflow.

| Plugin | Type | How it helps | Connectors |
|--------|------|-------------|------------|
| **[financial analysis](./financial-analysis)** | Core (install first) | Build comps, DCF models, LBO models, and 3-statement financials. QC presentations and create reusable PPT templates. Provides the shared foundation and all data connectors. | Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, Egnyte |
| **[investment banking](./investment-banking)** | Add-on | Draft CIMs, teasers, and process letters. Build buyer lists, run merger models, create strip profiles, and track live deals through milestones. | — |
| **[equity research](./equity-research)** | Add-on | Write earnings updates and initiating coverage reports. Maintain investment theses, track catalysts, draft morning notes, and screen for new ideas. | — |
| **[private equity](./private-equity)** | Add-on | Source and screen deals, run due diligence checklists, analyze unit economics and returns, draft IC memos, and monitor portfolio company KPIs. | — |
| **[wealth management](./wealth-management)** | Add-on | Prep for client meetings, build financial plans, rebalance portfolios, generate client reports, and identify tax-loss harvesting opportunities. | — |

**41 skills, 38 commands, 11 MCP integrations**

Install these directly from Cowork, browse the full collection here on GitHub, or build your own.

### Partner-Built Plugins

These plugins are built and maintained by our data partners, bringing their financial data and analytics directly into Claude workflows.

| Plugin | Partner | How it helps |
|--------|---------|-------------|
| **[LSEG](./partner-built/lseg)** | [LSEG](https://www.lseg.com/) | Price bonds, analyze yield curves, evaluate FX carry trades, value options, and build macro dashboards using LSEG financial data and analytics. 8 commands covering fixed income, FX, equities, and macro. |
| **[S&P Global](./partner-built/spglobal)** | [S&P Global](https://www.spglobal.com/) | Generate company tearsheets, earnings previews, and fun