# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Flask-based web app for tracking Pokemon shiny encounters. Currently in early development — minimal skeleton with a single route.

## Setup & Running

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server (hot-reload enabled via debug=True)
python src/app.py
```

The server runs at `http://127.0.0.1:5000` by default.

## Architecture

- **Entry point:** `src/app.py` — Flask app instance, routes defined here
- **Tech stack:** Python + Flask 3.1.3, Jinja2 for templating, Werkzeug for WSGI
- **No database yet** — when added, likely SQLite via SQLAlchemy (`.sqlite3` files are already gitignored)
- **No tests yet** — no test runner configured

## Dependency Management

Python dependencies are pinned in `requirements.txt`. Use `pip freeze > requirements.txt` after installing new packages.
