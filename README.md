# Software QA & Testing — Assignment 5 (AITU)

![Python](https://img.shields.io/badge/python-3.11-blue)
![Selenium](https://img.shields.io/badge/tool-Selenium-43B02A)
![pytest](https://img.shields.io/badge/runner-pytest-0A9EDC)
![pytest-html](https://img.shields.io/badge/report-pytest--html-orange)

## Overview

Assignment 5 for the **Software Quality Assurance and Testing** course at Astana IT University.
Focuses on **test lifecycle management**, **structured logging**, and **HTML reporting** in
Python — concepts equivalent to TestNG annotations and Log4j used in Java-based SQAT courses.
Target site: [the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login).

## What it covers

- **pytest fixtures with scopes** — session, class, and function level lifecycle hooks
  (equivalent to `@BeforeSuite`/`@AfterSuite`, `@BeforeClass`/`@AfterClass`, `@BeforeMethod`/`@AfterMethod`)
- **Structured logging** — `logging` module with console and file handlers (equivalent to Log4j)
- **pytest-html reports** — automatic HTML report with embedded screenshots on test failure
- **Page Object Model** — `LoginPage` class with locator constants and action methods
- **Driver factory** — centralized `create_driver()` with headless support via `HEADLESS=1` env var
- **Screenshot hook** — `pytest_runtest_makereport` captures screenshots on failure and embeds
  them in the HTML report
- Valid and invalid login scenarios with flash-message assertions

## Project structure

```
Assignment_5_SQAT/
├── pages/
│   └── login_page.py         # LoginPage POM class
├── tests/
│   ├── conftest.py           # Fixtures: session/class/function setup + screenshot hook
│   └── test_login.py         # Test class with valid and invalid login cases
├── utils/
│   ├── driver_factory.py     # Chrome WebDriver factory (headless-capable)
│   ├── logging_config.py     # Logging setup (console + file)
│   └── screenshot.py         # Screenshot helper used by the conftest hook
├── reports/
│   └── pytest-report.html    # Generated HTML report from last run
├── pytest.ini                # pytest config (--html report path, testpaths)
└── requirements.txt
```

## Getting started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run headless:

```bash
HEADLESS=1 pytest
```

### Output

| Artifact | Path |
|---|---|
| HTML report | `reports/pytest-report.html` |
| Log file | `reports/test-run.log` |
| Failure screenshots | `reports/screenshots/` |

---

Adil Ormanov — [GitHub](https://github.com/Adilforest)
