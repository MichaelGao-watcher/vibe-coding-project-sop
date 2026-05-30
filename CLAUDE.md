# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

vibe-coding-project-sop is the **mother library** for AI-assisted development workflow. It provides a standardized 5-phase SOP, reusable templates, Python automation scripts, and cross-project knowledge aggregation (94 lessons-learned, 200+ troubleshooting entries, 30+ ADRs from downstream projects).

## Key entry points

- `AGENTS.md` — hard rules, module index, trigger-word commands (存档/恢复/拉取母库/聚合). Read first on any session.
- `status.md` — current progress, todo list, environment notes
- `session-log.md` — session history for context recovery
- `skeleton-manifest.json` — machine-readable skeleton metadata and file contracts

## Architecture

This repo has two roles in one:

1. **Mother library**: Aggregates knowledge from downstream projects via `scripts/sync-knowledge.py`, consuming `config/github-sync.json`. Knowledge files (`decisions.md`, `lessons-learned.md`, `troubleshooting.md`) live at root and contain merged content from all synced repos, each entry tagged with source.

2. **Template skeleton**: `templates/` holds clean starting files that `scripts/init-skeleton.py` copies into new projects. `starter/` is a pre-assembled subset of `templates/` for quick bootstrapping. The separation ensures template purity — knowledge files are stored at root, not in `templates/`.

## Scripts

| Script | Purpose | Run with |
|--------|---------|----------|
| `scripts/init-skeleton.py` | One-click init: copy infrastructure files + optional knowledge seed to a target project | `python scripts/init-skeleton.py --skeleton . --with-knowledge` |
| `scripts/sync-knowledge.py` | Aggregate knowledge from GitHub repos into the mother library | `python scripts/sync-knowledge.py` |
| `scripts/build-experience-index.py` | Auto-generate unified `experience-index.md` from troubleshooting + lessons-learned + decisions | `python3 scripts/build-experience-index.py` |
| `scripts/pull.py` | Quick pull of mother-library files into a downstream project | `python pull.py` |

Requires Python 3.9+. Only `sync-knowledge.py` has an external dependency (`requests`).

## Trigger-word commands

These are natural-language commands parsed from `AGENTS.md` that trigger multi-step workflows:

- **存档** (exact match): Full archive flow — update status.md, append session-log.md, optionally update troubleshooting/lessons-learned/decisions, then git commit + push.
- **恢复** (exact match): Recovery flow — git pull, read status.md + session-log.md, report state summary.
- **拉取母库 / 拉取经验 / 更新经验** (exact match): Pull mother-library experience into current project.
- **聚合** (exact match): Aggregate experience from all repos into the mother library.

## Hard rules (from AGENTS.md)

- **RULE-01**: Infrastructure layer (AGENTS.md, status.md, session-log.md, vibe-coding-sop.md, etc.) must be established before creating any phase outputs.
- **RULE-02**: Phase boundaries = session boundaries. Stop after each phase, don't push into the next.
- **ARCHIVE-01/02**: "存档" triggers confirmation-first archive workflow; never skip confirmation.
- **RULE-05**: Knowledge sync must backup before merge, tag every entry with `[来源:repo @date]`.
- **RULE-07**: `experience-index.md` is auto-generated (by `scripts/build-experience-index.py`), never edit it manually.
- **RULE-08**: Before adding new modules, search for existing reusable components. Never rewrite what already exists.

## Git conventions

- Commit messages use `[session]` prefix for archive commits, `[feature]` for feature work.
- Branch `master` is the default (not `main`).
- Push uses HTTPS + GitHub CLI (`gh auth setup-git`), not SSH.
- `.gitattributes` enforces LF line endings on all text files.
