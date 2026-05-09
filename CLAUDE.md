# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal learning workspace as the user (re)visits Python fundamentals by coding along with Dave Ebbelaar's "Python for AI - Complete Beginner Course" ([YouTube](https://youtu.be/ygXn5nV5qFc)). It is **not** a product or library — it is a progressive, milestone-driven course codebase. Code added here corresponds to lessons being worked through, in order. Treat additions as pedagogical examples first, production code second.

The companion handbook the course references is at **https://python.datalumina.com/llms.txt** — when the user asks about a topic covered in the course (e.g., "the section on dictionaries", "what does the handbook say about virtual environments"), fetch that URL with WebFetch before answering. It is the authoritative source for what "the course" teaches and the order topics appear in.

## Toolchain — strict

- **Package manager: `uv` only. Do not use `pip`.** The user has explicitly chosen the modern uv-based workflow; running `pip install` would bypass the lockfile and contradict the learning goal. Add dependencies with `uv add <pkg>`, run scripts with `uv run <cmd>`, and let uv manage `.venv/` automatically.
- **Python: 3.12+** (pinned via `.python-version`, declared in `pyproject.toml`).
- **Virtual env: `.venv/`** at repo root, created/managed by uv. Already gitignored.
- **Formatter/linter:** Ruff is on the course syllabus but not yet configured. When the lesson on Ruff is reached, add it via `uv add --dev ruff` and configure in `pyproject.toml`.

Common commands:
```
uv sync                  # install/sync deps from pyproject.toml + uv.lock
uv add <pkg>             # add a runtime dependency
uv add --dev <pkg>       # add a dev dependency
uv run python main.py    # run a script inside the managed venv
uv run python -m <mod>   # run a module
```

## Repository shape and how it will grow

Current state is the bare `uv init` scaffold (`main.py`, `pyproject.toml`, `.python-version`). The repo will accumulate as lessons progress. Expected trajectory, per `README.md`:

1. Setup & professional workflow (uv, venv, VS Code, git)
2. Python basics (variables, types, control flow, data structures)
3. Building programs (functions, error handling, OOP)
4. External tools & APIs (`requests`, `pandas`, `matplotlib`, web scraping)
5. Production practices (multi-module organization, Ruff, `.env` for secrets, git/GitHub)

A `docs/` folder is planned for deeper technical notes and cheat sheets (per `README.md`); keep README focused on usage and put long-form explanations in `docs/` when that folder appears.

## How to assist the user effectively

- The user is **refreshing**, not learning Python from zero. Skip basic preamble; explain the *why* and edge cases. Frame new concepts in relation to ones already covered in earlier lessons of the repo.
- When adding code for a lesson, mirror the course's progression — do not jump ahead to advanced patterns (decorators, type generics, async) before the corresponding lesson is reached. If unsure where the user is, check recent commits and the latest files added.
- For API/secret work later in the course: secrets go in `.env` (already gitignored), loaded via `python-dotenv` or similar. Never hardcode keys in example code, even pedagogical.
- When a topic is ambiguous ("how should we structure this?"), the handbook at `python.datalumina.com/llms.txt` is the tiebreaker — it reflects what the course teaches.
