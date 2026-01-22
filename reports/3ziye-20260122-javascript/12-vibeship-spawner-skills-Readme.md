# Spawner Skills

> **[spawner.vibeship.co](https://spawner.vibeship.co)** | **[Browse All Skills](https://spawner.vibeship.co/skills)**

**462 production-grade skills** for Claude. Zero cost, works offline. Full MCP integration.

## Why Spawner Skills?

Most "AI prompts" are just text files. Spawner Skills are **production-grade knowledge systems** with 4 specialized files per skill:

```
maker/micro-saas-launcher/
├── skill.yaml           # Identity, patterns, anti-patterns, handoffs
├── sharp-edges.yaml     # Gotchas with detection patterns
├── validations.yaml     # Automated code quality checks
└── collaboration.yaml   # How skills work together
```

### What Makes Our Skills Different

| Feature | Regular Prompts | Spawner Skills |
|---------|-----------------|----------------|
| **Patterns** | Generic advice | Battle-tested implementation code |
| **Anti-patterns** | None | "Don't do this because..." with alternatives |
| **Sharp Edges** | None | Gotchas with automatic detection |
| **Validations** | None | Regex patterns that catch mistakes |
| **Collaboration** | None | Skills delegate to each other |
| **Severity Levels** | None | Critical, high, medium, low |

---

## Quick Start

```bash
# Full setup: Skills + MCP server (recommended)
npx github:vibeforge1111/vibeship-spawner-skills install --mcp
```

This one command:
- Installs 462 skills to `~/.spawner/skills/`
- Configures the Spawner MCP server for Claude Desktop & Claude Code
- Enables project memory, code validation, sharp edge detection

### Other Commands

```bash
# Just install skills (no MCP)
npx github:vibeforge1111/vibeship-spawner-skills install

# Add MCP to existing installation
npx github:vibeforge1111/vibeship-spawner-skills setup-mcp

# Update skills to latest
npx github:vibeforge1111/vibeship-spawner-skills update

# Check status
npx github:vibeforge1111/vibeship-spawner-skills status
```

### Manual Clone (Alternative)

```bash
git clone https://github.com/vibeforge1111/vibeship-spawner-skills ~/.spawner/skills
```

---

## The 4-File Skill System

### 1. `skill.yaml` - Identity & Patterns

Defines who the skill is and how it works:

```yaml
id: micro-saas-launcher
name: Micro-SaaS Launcher
identity:
  role: SaaS Launch Architect
  personality: |
    You've launched 12 micro-SaaS products. You know the difference
    between "building" and "shipping." You push for MVP ruthlessly.

patterns:
  - name: 2-Week MVP
    when_to_use: Starting any new SaaS
    implementation: |
      Week 1: Core feature + auth + payments
      Week 2: Landing page + launch

anti_patterns:
  - name: Feature Creep Before Launch
    why_bad: You'll never ship. Users don't want features, they want solutions.
    what_to_do_instead: Launch with ONE core feature. Add more based on feedback.

handoffs:
  - trigger: "landing page|sales page"
    to: landing-page-design
    context: "SaaS landing page needed"
```

### 2. `sharp-edges.yaml` - Gotchas & Warnings

Things that bite you in production:

```yaml
sharp_edges:
  - id: no-distribution-plan
    summary: Building without knowing how to reach customers
    severity: critical
    situation: You're building but have no idea where customers will come from
    why: |
      Distribution is harder than building.
      "If you build it, they will come" is a lie.
      Most failed startups had good products, bad distribution.
    solution: |
      ## Before Writing Code, Answer:

      | Question | Your Answer |
      |----------|-------------|
      | Where do your customers hang out? | _________ |
      | Can you reach 100 of them this week? | _________ |
      | What's your unfair distribution advantage? | _________ |

      If you can't answer these, STOP BUILDING.
    symptoms:
      - "I'll figure out marketing later"
      - "The product will sell itself"
      - Building for 3+ months with no users
    detection_pattern: "marketing later|users will come|viral"
```

### 3. `validations.yaml` - Automated Code Checks

Catch mistakes before they ship:

```yaml
validations:
  - id: no-payment-integration
    name: No Payment Integration
    severity: critical
    type: conceptual
    check: "SaaS should have payment integration"
    indicators:
      - "No Stripe/payment code"
      - "Free tier only"
      - "Payment coming soon"
    message: "No payment integration - you're building a hobby, not a business."
    fix_action: "Add Stripe checkout before launch. No exceptions."

  - id: api-key-exposed
    name: API Key in Frontend Code
    severity: critical
    type: regex
    pattern: '(sk_live_|sk_test_)[a-zA-Z0-9]{20,}'
    file_patterns:
      - "*.js"
      - "*.ts"
      - "*.tsx"
    message: "Stripe secret key exposed in frontend code!"
    fix_action: "Move to environment variables on backend"
```

### 4. `collaboration.yaml` - Skill Teamwork

How skills work together:

```yaml
receives_from:
  - skill: landing-page-design
    context: "SaaS landing page"
    receives:
      - "Conversion-optimize