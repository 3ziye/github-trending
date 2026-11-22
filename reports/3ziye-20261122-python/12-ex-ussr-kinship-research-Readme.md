# ex-USSR Kinship Research

![ex-USSR Kinship Research cover](docs/cover.jpg)

Languages: [English](README.md) / [Русский](README.ru.md) / [Беларуская](README.be.md) / [Қазақша](README.kk.md) / [Українська](README.uk.md) / [Polski](README.pl.md) / [Deutsch](README.de.md) / [Română](README.ro.md) / [Eesti](README.et.md) / [Latviešu](README.lv.md) / [Lietuvių](README.lt.md) / [ქართული](README.ka.md) / [Հայերեն](README.hy.md) / [Azərbaycanca](README.az.md) / [Кыргызча](README.ky.md) / [Тоҷикӣ](README.tg.md) / [Türkmençe](README.tk.md) / [O‘zbekcha](README.uz.md) / [日本語](README.ja.md)

**An evidence-first genealogy skill for AI agents (Codex, Claude Code and other Agent Skills runtimes).** It turns an agent into a careful family-history researcher for the former USSR, the Soviet Union and the Russian Empire. The agent reads church books and civil records, military, deportation and repression files, and unindexed archive scans. It keeps every find traceable, separates records from interpretation and says plainly what is proven and what is not.

Coverage includes all 15 former Soviet republics: Russia, Ukraine, Belarus, Moldova, Estonia, Latvia, Lithuania, Georgia, Armenia, Azerbaijan, Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan and Uzbekistan. Archives are chosen by the event's historical jurisdiction and current record custodian; a regional example does not replace local research.

The skill's instructions are written in Russian, but **the agent talks to you in your language**: English, Ukrainian, Russian, Polish, German and so on. It quotes sources in their original spelling with a translation, and builds search queries in the languages of the records.

---

## What it does

- **Case intake and scope.** One research question, known facts, who may be alive, what is off-limits.
- **Reproducible registers.** Persons, artifacts, claims, relationships and a full search log (CSV), plus a final report template.
- **Historical jurisdiction model.** It resolves every event to the state, province, district, parish or civil registry *as of the event date*, not today's map.
- **Name-variant matrices.** Pre-reform Russian, Ukrainian, Polish, Romanian, German and Yiddish forms, patronymics, maiden names and transliterations.
- **Source strategy.** Originals first, then official catalogs, indexes, published document collections, and only then trees and forums as leads.
- **Evidence protocol.** Claims get explainable statuses, not percentages: `hypothesis`, `single-source`, `corroborated`, `strongly-corroborated`, `contradicted`, `unresolved`. Copies and mirrors of one record share an `independence_group`, so they never count as independent proof.
- **Identity resolution.** Namesakes stay separate `person_id`s until distinguishing evidence appears: house number, parents, godparents, exact birth date or military unit.
- **Audit script.** It checks referential integrity and flags weak corroboration before you write conclusions. An independence group counts only when a cited artifact belongs to it, so corroboration cannot be declared into existence. It also checks IDs and statuses in the working Markdown report, if present; the agent checks the delivered HTML against the registers. A summary shows what is still uncorroborated or marked illegible.
- **Institutional requests.** Draft and, when authorized, send focused requests to archives, libraries, universities and museums using available email or official web tools. If needed, offer a supported mail integration or a ready-to-send letter. Record the outcome, avoid duplicate sends and treat replies as evidence. See [correspondence guidance](references/correspondence.md).
- **Archive request form.** An anonymized [CANO vital-record request template](assets/cano-vital-record-request.template.docx) preserves the supplied form's layout for an editable case copy. Verify the archive's current form and submission requirements before use.
- **Government services.** Choose an official civil-registration or archive request route, checking eligibility and how the result is delivered ([government portals](references/government-portals.md)).
- **Final report.** A complete HTML report is the default deliverable, with each relationship laid out edge by edge, contradictions, failed searches and concrete next steps. PDF is an optional export only when you explicitly request it.
- **Targeted indexed-record research.** Find relevant FamilySearch books by place or DGS through an existing lawful browser session, view specific records, and retain only evidence fragments permitted by the source. Local helpers search relatives, witnesses and name variants in saved fragments, preserving their context and file checksums. [Workflow and coverage limits](references/familysearch-indexes.md).
- **Connected FamilySearch MCP.** Use a connected server for structured searches, profiles, relatives and sources, and authorized tree changes with explicit scope and read-back. Keep indexed search separate from unin