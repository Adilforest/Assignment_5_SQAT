import logging
from pathlib import Path

def configure_logging() -> None:
    """Configure logging similar to Log4j (console + file)."""
    logs_dir = Path("reports")
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_file = logs_dir / "test-run.log"

    root = logging.getLogger()
    root.setLevel(logging.INFO)

    # Avoid duplicate handlers if called multiple times
    if root.handlers:
        return

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(fmt)

    fileh = logging.FileHandler(log_file, encoding="utf-8")
    fileh.setLevel(logging.INFO)
    fileh.setFormatter(fmt)

    root.addHandler(console)
    root.addHandler(fileh)
