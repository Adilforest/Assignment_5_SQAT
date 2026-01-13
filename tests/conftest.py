import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import logging
import pytest

from utils.logging_config import configure_logging
from utils.driver_factory import create_driver
from utils.screenshot import save_screenshot

log = logging.getLogger("conftest")

# --- Equivalent of @BeforeSuite / @AfterSuite ---
@pytest.fixture(scope="session", autouse=True)
def session_setup_teardown():
    configure_logging()
    log.info("=== TEST SUITE STARTED (session) ===")
    yield
    log.info("=== TEST SUITE FINISHED (session) ===")

# --- Equivalent of @BeforeClass / @AfterClass ---
@pytest.fixture(scope="class", autouse=True)
def class_setup_teardown(request):
    log.info(f"--- TEST CLASS STARTED: {request.node.name} ---")
    yield
    log.info(f"--- TEST CLASS FINISHED: {request.node.name} ---")

# --- Equivalent of @BeforeMethod / @AfterMethod ---
@pytest.fixture(scope="function")
def driver(request):
    log.info(f"Driver setup for test: {request.node.name}")
    d = create_driver()
    yield d
    log.info(f"Driver teardown for test: {request.node.name}")
    d.quit()

# --- Hook: take screenshot on failure and attach to pytest-html report ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("driver", None)
        if drv is not None:
            path = save_screenshot(drv, item.name)
            extra = getattr(rep, "extra", [])
            try:
                from pytest_html import extras
                extra.append(extras.image(str(path)))
            except Exception:
                pass
            rep.extra = extra
