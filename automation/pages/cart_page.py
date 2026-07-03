from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class CartPage(BasePage):
    """
    Page Object representing the Shopping Cart and Checkout workflows.
    """
    # Locators
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-btn")
    CART_HEADER_COUNT = (By.CLASS_NAME, "cart-count")
    CART_ITEM_LIST = (By.CLASS_NAME, "cart-item")
    PROCEED_TO_CHECKOUT = (By.ID, "checkout-btn")
    
    # Shipping Fields
    SHIPPING_ADDRESS = (By.ID, "ship-address")
    SHIPPING_ZIP = (By.ID, "ship-zip")
    SHIPPING_PHONE = (By.ID, "ship-phone")
    SUBMIT_ADDRESS = (By.ID, "ship-submit-btn")
    
    # Payment Fields
    CARD_NUMBER = (By.ID, "card-num")
    CARD_EXPIRY = (By.ID, "card-exp")
    CARD_CVV = (By.ID, "card-cvv")
    PAY_NOW_BUTTON = (By.ID, "pay-btn")
    
    ORDER_CONFIRMATION_MSG = (By.CLASS_NAME, "order-success-msg")
    ERROR_VALIDATION_MSG = (By.CLASS_NAME, "validation-error-msg")

    def __init__(self, driver):
        super().__init__(driver)

    def add_current_product_to_cart(self):
        """Adds currently loaded product page to cart."""
        self.click(self.ADD_TO_CART_BUTTON)

    def get_cart_count(self):
        """Gets count of items displayed in navigation bar header."""
        return self.get_text(self.CART_HEADER_COUNT)

    def proceed_to_checkout(self):
        """Clicks checkout from cart page."""
        self.click(self.PROCEED_TO_CHECKOUT)

    def fill_shipping_address(self, address, zip_code, phone):
        """Fills shipping address page fields and submits."""
        self.enter_text(self.SHIPPING_ADDRESS, address)
        self.enter_text(self.SHIPPING_ZIP, zip_code)
        self.enter_text(self.SHIPPING_PHONE, phone)
        self.click(self.SUBMIT_ADDRESS)

    def process_payment(self, card, expiry, cvv):
        """Fills payment card fields and triggers transaction."""
        self.enter_text(self.CARD_NUMBER, card)
        self.enter_text(self.CARD_EXPIRY, expiry)
        self.enter_text(self.CARD_CVV, cvv)
        self.click(self.PAY_NOW_BUTTON)

    def get_order_confirmation(self):
        """Retrieves success string for complete purchases."""
        return self.get_text(self.ORDER_CONFIRMATION_MSG)

    def get_validation_error(self):
        """Retrieves validation error message from checkout form."""
        return self.get_text(self.ERROR_VALIDATION_MSG)
