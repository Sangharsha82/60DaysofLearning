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

On Windows using CMD:

```cmd
webapp\Scripts\activate.bat
python -m pip install --upgrade pip
```

If you prefer to create a fresh virtual environment instead of using the included `webapp/`, run:

```bash
python -m venv .venv
.\venv\Scripts\activate
pip install --upgrade pip
```

## Usage

Run the Day 2 script with the active virtual environment:

```bash
python day2.py
```

## Notes

- The `webapp/` folder contains a full virtual environment. It's recommended to add `webapp/` to `.gitignore` to avoid committing environment-specific files.
- If you want help turning this into a small web app or adding tests, open an issue or request changes.

## Contributing

Contributions are welcome. For small changes, open a pull request describing the changes.

## License

This project is unlicensed. Add a license (for example, MIT) if you want to allow reuse.
