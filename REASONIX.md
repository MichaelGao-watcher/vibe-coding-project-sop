# REASONIX.md — vibe-coding-project-sop

## Stack

- **Python 3.9+** — all automation scripts, no formal package (no `pyproject.toml`)
- **No external deps** except `requests` (only `sync-knowledge.py` needs it)
- **Markdown** — all knowledge artifacts (decisions, lessons, troubleshooting) are `.md` files
- **CLAUDE.md / AGENTS.md** — dual-agent-entry-point pattern for AI-assisted dev workflow

## Layout

- **Root (`AGENTS.md`, `CLAUDE.md`, `README.md`)** — entry points; `AGENTS.md` has hard rules + trigger words
- **`scripts/`** — Python automation: `init-skeleton.py`, `sync-knowledge.py`, `build-experience-index.py`, `pull.py`
- **`templates/`** — clean starting files for downstream projects (copy, don't edit)
- **`starter/`** — pre-assembled subset of templates for quick bootstrapping
- **`config/`** — `github-sync.json` (repo list for knowledge aggregation)
- **`*.md` at root** — knowledge files: `decisions.md`, `lessons-learned.md`, `troubleshooting.md`, `status.md`, `session-log.md`, `experience-index.md`
- **`.backup/`** — auto-generated backups from `sync-knowledge.py`

## Commands

```sh
python scripts/init-skeleton.py --skeleton . --with-knowledge   # Init downstream project
python scripts/sync-knowledge.py                                # Aggregate knowledge from GitHub
python3 scripts/build-experience-index.py                       # Rebuild experience-index.md
python scripts/pull.py                                          # Pull mother-library files into downstream
```

No test runner / linter / formatter detected.

## Conventions

- **LF line endings** enforced by `.gitattributes` on all text files
- **Commit prefixes**: `[session]` for archive commits, `[feature]` for feature work
- **Branch**: `master` (not `main`)
- **Git push** uses HTTPS + GitHub CLI (`gh auth setup-git`), not SSH
- **Chinese** docstrings and comments throughout
- **All Python scripts** have `#!/usr/bin/env python3` shebang and argparse

## Watch out for

- **`experience-index.md` is auto-generated** (by `scripts/build-experience-index.py`) — never edit it by hand (RULE-07 in AGENTS.md)
- **`templates/` files must be copied, not edited in place** — they are source templates for downstream projects
- **No `pyproject.toml` / `requirements.txt`** — scripts run directly; only `sync-knowledge.py` needs `pip install requests`
- **`skeleton-manifest.json`** defines the init protocol: infrastructure layer first, phase outputs second — skip ordering at your own risk
