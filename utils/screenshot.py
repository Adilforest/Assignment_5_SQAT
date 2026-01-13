from pathlib import Path
from datetime import datetime

def save_screenshot(driver, test_name: str) -> Path:
    out_dir = Path("reports") / "screenshots"
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe = "".join(c if c.isalnum() or c in "._-" else "_" for c in test_name)
    path = out_dir / f"{safe}_{ts}.png"
    driver.save_screenshot(str(path))
    return path
