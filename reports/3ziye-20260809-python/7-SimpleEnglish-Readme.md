<p align="center">
  <strong>✈️ your AI writes like a LinkedIn post. make it write like a Boeing manual.</strong>
</p>

<p align="center">
  An agent skill that forces LLMs to write docs in <a href="https://www.asd-ste100.org/">ASD-STE100 Simplified Technical English</a>:<br>
  the controlled language aerospace has used since 1983 so a tired mechanic <em>cannot</em> misread an instruction.<br>
  AI slop dies as a side effect. 💀
</p>

<p align="center">
  <a href="evals/results/RESULTS.md"><img src="https://img.shields.io/badge/STE_violations-%E2%88%9272.9%25_measured-brightgreen?style=flat" alt="72.9% fewer violations, measured"></a>
  <a href="evals/results/RESULTS.md"><img src="https://img.shields.io/badge/benchmarked_on-6_Claude_models-blueviolet?style=flat" alt="6 models benchmarked"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/SKILL.md-open_standard-blue?style=flat" alt="Agent Skills"></a>
  <a href="skills/simple-english/SKILL.md"><img src="https://img.shields.io/badge/version-1.2.0-blue?style=flat" alt="version 1.2.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat" alt="MIT"></a>
  <a href="https://github.com/AminBlg/SimpleEnglish/stargazers"><img src="https://img.shields.io/github/stars/AminBlg/SimpleEnglish?style=flat&logo=github&color=yellow" alt="GitHub stars"></a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/97933?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-97933" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/97933/daily?language=Python" alt="AminBlg%2FSimpleEnglish | Trendshift" width="250" height="55"/></a>
  <a href="https://trendshift.io/repositories/97933?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-97933" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/97933/daily" alt="AminBlg%2FSimpleEnglish | Trendshift" width="250" height="55"/></a>
</p>

<p align="center">
  <a href="#-before--after">See it</a> ·
  <a href="#-install">Install</a> ·
  <a href="#-the-rules">The rules</a> ·
  <a href="#-not-just-docs">Not just docs</a> ·
  <a href="#-receipts">Receipts</a> ·
  <a href="#-faq">FAQ</a>
</p>

---

Works in every harness that speaks the [Agent Skills standard](https://agentskills.io): Claude Code, Cursor, VS Code Copilot, OpenAI Codex, Gemini CLI, Goose, OpenCode, and ~25 more. One folder, no dependencies, MIT.

## 🔥 Before / after

Left column is **real unedited Claude output**. Right column is the same model with the skill loaded.

<table>
<tr>
<th width="50%">🤖 Without skill</th>
<th width="50%">✈️ With skill</th>
</tr>
<tr>
<td valign="top">

> Leveraging sqlpipe's robust architecture, users can seamlessly synchronize their Postgres tables to S3 with minimal configuration overhead. Before getting started, you should ensure that your AWS credentials have been properly configured — this is crucial for avoiding frustrating permission issues down the line.

</td>
<td valign="top">

> sqlpipe copies your Postgres tables to S3. It needs one configuration file.
>
> Before you start, make sure that your AWS credentials are correct. If they are not, S3 rejects the upload with a permission error.

</td>
</tr>
<tr>
<td valign="top">

> Oops! Something went wrong while attempting to establish a connection. Please ensure your credentials have been properly configured and try again, or reach out to your administrator if the issue persists.

</td>
<td valign="top">

> Connection to the database failed: the password for user `app` was not correct.
> Set `DB_PASSWORD` to the correct value, then connect again.

</td>
</tr>
<tr>
<td valign="top">

> We have identified an issue that may have impacted some users' ability to access the service. We sincerely apologize for any inconvenience this may have caused.

</td>
<td valign="top">

> Between 14:02 and 14:31 UTC, 12% of requests failed. A deploy at 14:00 removed the cache warmup step. We reverted it at 14:27.

</td>
</tr>
</table>

More rewrites in [`examples/before-after.md`](examples/before-after.md): READMEs, error messages, incident reports, release notes.

## 📦 Install

```bash
npx skills add AminBlg/SimpleEnglish
```

That is it. The [skills CLI](https://github.com/vercel-labs/skills) detects your agents (Claude Code, Cursor, Codex, Copilot, Gemini CLI, and more) and installs for the ones you pick. Try before installing:

```bash
npx skills use AminBlg/SimpleEnglish@simple-english
```

**Claude Code plugin**: this repo is also a plugin marketplace. From your terminal:

```bash
claude plugin marketplace add AminBlg/SimpleEnglish && claude plugin install simple-english@simple-english
```

Or inside Claude Code: `/plugin marketplace add AminBlg/SimpleEnglish`, then `/plugin install simple-english@simple-english`.

**Output style** (Claude Code): the 