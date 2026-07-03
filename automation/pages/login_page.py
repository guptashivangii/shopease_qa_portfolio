from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Page Object representing the User Login/Logout page.
    """
    # Locators
    USERNAME_FIELD = (By.ID, "login-username")
    PASSWORD_FIELD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    LOGOUT_BUTTON = (By.ID, "logout-btn")
    ERROR_ALERT = (By.CLASS_NAME, "login-error-msg")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        """Logs into the application."""
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def logout(self):
        """Logs out from the active session."""
        self.click(self.LOGOUT_BUTTON)

    def get_error_message(self):
        """Retrieves error message from login view."""
        return self.get_text(self.ERROR_ALERT)

    def is_logged_in(self):
        """Verifies session status by checking logout button presence."""
        return self.is_element_displayed(self.LOGOUT_BUTTON)
