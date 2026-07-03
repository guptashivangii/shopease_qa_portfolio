from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class RegistrationPage(BasePage):
    """
    Page Object representing the User Registration page.
    """
    # Locators (Using IDs/Names as best practice for QA testability)
    USERNAME_FIELD = (By.ID, "reg-username")
    EMAIL_FIELD = (By.ID, "reg-email")
    PASSWORD_FIELD = (By.ID, "reg-password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "reg-confirm-password")
    SUBMIT_BUTTON = (By.ID, "reg-submit-btn")
    ERROR_ALERT = (By.CLASS_NAME, "reg-error-msg")
    SUCCESS_ALERT = (By.CLASS_NAME, "reg-success-msg")

    def __init__(self, driver):
        super().__init__(driver)

    def register(self, username, email, password, confirm_password):
        """Fills the registration form and submits it."""
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.enter_text(self.CONFIRM_PASSWORD_FIELD, confirm_password)
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self):
        """Retrieves error message from registration page."""
        return self.get_text(self.ERROR_ALERT)

    def get_success_message(self):
        """Retrieves success message from registration page."""
        return self.get_text(self.SUCCESS_ALERT)
