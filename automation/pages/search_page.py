from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class SearchPage(BasePage):
    """
    Page Object representing the Product Catalog Search page.
    """
    # Locators
    SEARCH_INPUT = (By.ID, "search-input")
    SEARCH_BUTTON = (By.ID, "search-submit-btn")
    PRODUCT_ITEM_TITLE = (By.CLASS_NAME, "product-title")
    NO_RESULTS_MESSAGE = (By.CLASS_NAME, "no-results-msg")
    CATEGORY_CHECKBOX = (By.CSS_SELECTOR, "input[value='Electronics']")
    PRICE_MIN_FIELD = (By.ID, "price-min")
    PRICE_MAX_FIELD = (By.ID, "price-max")

    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self, keyword):
        """Searches for products using a keyword."""
        self.enter_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)

    def filter_by_category(self):
        """Filters search results by category."""
        self.click(self.CATEGORY_CHECKBOX)

    def get_search_results(self):
        """Returns list of product titles displayed on search results page."""
        try:
            elements = self.driver.find_elements(*self.PRODUCT_ITEM_TITLE)
            return [element.text for element in elements]
        except Exception:
            return []

    def get_no_results_message(self):
        """Returns no results found message if query matches nothing."""
        return self.get_text(self.NO_RESULTS_MESSAGE)
