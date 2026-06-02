# 60DaysofLearning — Day 2

Brief summary for this repository and how to run the Day 2 code.

## Summary

This repo contains Day 2 work for the "60 Days of Learning" series. It includes a small Python script used for Day 2 exercises and a local Python virtual environment in the `webapp/` folder.

## Repository structure

- [day2.py](day2.py) — main Day 2 script
- [webapp/](webapp/) — local Python virtual environment and packages

## Setup

On Windows using PowerShell (recommended):

```powershell
# From repository root
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
webapp\Scripts\Activate.ps1
python -m pip install --upgrade pip
# install project requirements if any (example)
# pip install -r requirements.txt
```

# Day 2 Notes — Virtualenv, Dictionaries, and Error Handling

This file contains a short summary of what was learned on Day 2: working with Python virtual environments, common dictionary operations, and basic error handling patterns.

## Virtual Environments (venv)

Create a new virtual environment:

```powershell
python -m venv .venv
```

Activate (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate (CMD):

```cmd
.\.venv\Scripts\activate.bat
```

Activate (Bash / WSL / macOS):

```bash
source .venv/bin/activate
```

Deactivate (all shells):

```bash
deactivate
```

Notes:
- Use a project-local venv (like `.venv`) to avoid committing environment files.
- The included `webapp/` is a full virtual environment — prefer creating `.venv` instead.

## Dictionaries (Python)

- Create: `d = {}` or `d = {'a': 1, 'b': 2}`
- Access: `value = d['key']` (raises `KeyError`) or `value = d.get('key', default)`
- Add / Update: `d['new'] = 3`
- Remove: `d.pop('key')`, `del d['key']`
- Iterate keys/values/items:
  - `for k in d:`
  - `for k, v in d.items():`
- Useful methods: `d.keys()`, `d.values()`, `d.items()`, `d.update(other)`, `d.clear()`
- Dictionary comprehension example: `squares = {x: x*x for x in range(6)}`

## Error Handling (try / except)

Basic structure:

```python
try:
	# code that may raise
	value = int(user_input)
except ValueError:
	# handle specific error
	print('Please enter a valid integer')
except Exception as e:
	# catch-all (use sparingly)
	print('Unexpected error:', e)
else:
	# runs if no exception
	print('Parsed value:', value)
finally:
	# runs always
	cleanup()
```

Best practices:
- Catch specific exceptions (e.g., `ValueError`, `KeyError`) rather than a bare `except:`.
- Use `finally` for cleanup actions that must run regardless of errors.
- Prefer logging or re-raising when an error should bubble up.

---

If you'd like, I can add short example snippets in `day2.py` to demonstrate these concepts interactively.
