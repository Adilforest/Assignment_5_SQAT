# Assignment 5 SQAT (Python version)

This project implements the same **concepts** required in Assignment 5:
- Test lifecycle annotations (equivalent to TestNG) using pytest fixtures
- Logging (like Log4j) using Python `logging`
- Report + screenshots using `pytest-html` and screenshot capture on failure

## Install
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
pytest
```

Headless:
```bash
HEADLESS=1 pytest
```

## Outputs
- HTML report: `reports/pytest-report.html`
- Logs: `reports/test-run.log`
- Screenshots on failure: `reports/screenshots/`
