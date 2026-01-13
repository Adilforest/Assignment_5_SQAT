import logging
from pages.login_page import LoginPage

log = logging.getLogger(__name__)

class TestLogin:
    def test_invalid_login_shows_error(self, driver):
        log.info("Open login page")
        page = LoginPage(driver).open()

        log.info("Login with invalid credentials")
        page.login("wrong", "wrong")

        msg = page.flash_message().lower()
        log.info(f"Flash message: {msg}")

        assert "your username is invalid" in msg

    def test_valid_login_succeeds(self, driver):
        log.info("Open login page")
        page = LoginPage(driver).open()

        log.info("Login with valid credentials")
        page.login("tomsmith", "SuperSecretPassword!")

        msg = page.flash_message().lower()
        log.info(f"Flash message: {msg}")

        assert "you logged into a secure area" in msg
