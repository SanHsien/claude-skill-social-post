# social-post skill (Windows Maintenance Fork)

[繁體中文說明](README.md) · [Fork 維護說明](FORK.md)

A Claude Code and Codex skill by Hao (駱君昊) that learns your personal social media voice, plans high-performing content, drafts platform-tailored posts (FB, IG, Threads, X, YouTube), publishes after confirmation, manages comments via controlled Chrome browser actuation, and stores cross-platform insights into verifiable structured data.

This repository is a **Windows-first maintenance fork** of [`Hao0321/claude-skill-social-post`](https://github.com/Hao0321/claude-skill-social-post), maintaining full upstream git history, verified on Windows 11 with PowerShell 7 and GitHub Actions CI.

Current stable tag: **v2.5.0**; `main` synchronizes **Unreleased candidate**.

---

## Highlights & Validation

- **Mega-viral Validated**: 80K reach, 448 likes, 500 comments on first post. Includes day-by-day postmortem and formula iterations.
- **Voice Learning (P1)**: Analyzes your authentic writing style and builds local style profiles without leaking private training data.
- **14-Day Content Calendar (P0)**: Systematically structures campaigns across Facebook, Instagram, Threads, and X.
- **Drafting & Publishing Gates (P2)**: Multi-platform draft generation with strict human-in-the-loop confirmation before posting.
- **Outcome Ledger & Analytics (P3/P4)**: Append-only event store capturing raw text SHA, deterministic length, punctuation, formatting, and structured metrics.
- **Controlled Comment Ops (P5)**: Modular Chrome DOM actuator contract supporting target-only comment reading, provenance verification, and safe dry-run defaults.

---

## Quickstart & Installation

```powershell
git clone https://github.com/SanHsien/claude-skill-social-post.git
```

### Install into Codex (Windows PowerShell)

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse ".\claude-skill-social-post\social-post" "$env:USERPROFILE\.codex\skills\social-post"
```

### Install into Claude Code (Windows PowerShell)

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse ".\claude-skill-social-post\social-post" "$env:USERPROFILE\.claude\skills\social-post"
```

### Local Setup

In the installed `social-post/` directory:

```powershell
Copy-Item style_profile.example.md style_profile.md
Copy-Item content_plan.example.md content_plan.md
```

Personal profiles, drafts, and `data/` are kept private locally and excluded from git commits.

---

## The Six Operational Modes

| Mode | Purpose |
|---|---|
| **P0 Plan** | Plan campaigns, content buckets, and multi-platform experiments |
| **P1 Learn Voice** | Learn personal tone, pacing, and hooks from authorized writing samples |
| **P2 Draft / Publish** | Generate platform drafts; requires explicit per-round confirmation to publish |
| **P3 Log Outcome** | Record post snapshots, metrics, account insights, and corrections |
| **P4 Optimize Patterns** | Compare post variations across aligned maturity, platforms, and formats |
| **P5 Comment Ops** | Controlled Chrome comment scanning, drafting, and verified replies |

---

## Windows Maintenance & Development

For contributors and agents maintaining this fork:

```powershell
pwsh -NoProfile -File tools\bootstrap_dev.ps1
```

For more details on local development, architectural decisions, and upstream tracking:
- [Development Guide](docs/DEVELOPMENT.md)
- [Architecture Decisions](docs/DECISIONS.md)
- [Upstream Tracking](docs/UPSTREAM.md)
- [Review Snapshot](REVIEW.md)

---

## Upstream & License

This project is licensed under the [MIT License](LICENSE).
Original creator: Hao (駱君昊) and contributors to [`Hao0321/claude-skill-social-post`](https://github.com/Hao0321/claude-skill-social-post).