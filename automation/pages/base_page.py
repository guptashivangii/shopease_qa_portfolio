from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """
    The BasePage class provides wrappers for Selenium WebDriver interactions.
    All Page Objects inherit from this class to leverage dynamic waiting 
    and element interaction.
    """
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        """Finds an element in the DOM, waiting for its presence."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} not found within {self.timeout}s.")

    def find_visible_element(self, locator):
        """Finds an element, waiting for its visibility."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} was not visible within {self.timeout}s.")

    def click(self, locator):
        """Waits for an element to be clickable and performs click."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} was not clickable within {self.timeout}s.")

    def enter_text(self, locator, text):
        """Clears text input and enters new text value."""
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Retrieves text content of element."""
        return self.find_visible_element(locator).text

    def is_element_displayed(self, locator):
        """Checks whether element is displayed on page without throwing exception."""
        try:
            return self.find_visible_element(locator).is_displayed()
        except Exception:
            return False
