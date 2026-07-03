import pytest
from automation.pages.registration_page import RegistrationPage
from automation.pages.login_page import LoginPage
from automation.pages.search_page import SearchPage
from automation.pages.cart_page import CartPage

@pytest.mark.usefixtures("setup_driver")
class TestShopEaseStorefront:
    """
    Test suite executing core storefront automation workflows using the
    Page Object Model design framework.
    """
    BASE_URL = "http://shopease.qa"

    def test_01_user_registration_success(self):
        """Verifies successful registration with valid inputs."""
        self.driver.get(f"{self.BASE_URL}/register")
        reg_page = RegistrationPage(self.driver)
        
        reg_page.register(
            username="qa_tester_new",
            email="qa_tester_new@example.com",
            password="SecurePassword@123",
            confirm_password="SecurePassword@123"
        )
        
        # Verify success toast message
        success_msg = reg_page.get_success_message()
        assert "Account created successfully" in success_msg

    def test_02_user_registration_password_mismatch(self):
        """Verifies validation error on password mismatch."""
        self.driver.get(f"{self.BASE_URL}/register")
        reg_page = RegistrationPage(self.driver)
        
        reg_page.register(
            username="qa_tester_mismatch",
            email="mismatch@example.com",
            password="SecurePassword123",
            confirm_password="DifferentPassword123"
        )
        
        # Verify inline mismatch error message
        error_msg = reg_page.get_error_message()
        assert "Passwords do not match" in error_msg

    def test_03_login_success(self):
        """Verifies successful login using registered credentials."""
        self.driver.get(f"{self.BASE_URL}/login")
        login_page = LoginPage(self.driver)
        
        login_page.login(username="testuser1", password="Pass@1234")
        
        # Verify user state switches to logged in
        assert login_page.is_logged_in() is True

    def test_04_login_failure_invalid_credentials(self):
        """Verifies error message on invalid password entry."""
        self.driver.get(f"{self.BASE_URL}/login")
        login_page = LoginPage(self.driver)
        
        login_page.login(username="testuser1", password="WrongPassword")
        
        # Verify login failure notification
        error_msg = login_page.get_error_message()
        assert "Invalid credentials" in error_msg

    def test_05_product_search_and_filter(self):
        """Verifies search functionality and category filter integrations."""
        self.driver.get(f"{self.BASE_URL}/products")
        search_page = SearchPage(self.driver)
        
        search_page.search_product("iPhone 15")
        results = search_page.get_search_results()
        
        # Search results list should contain iPhone 15 product listing
        assert any("iPhone 15" in title for title in results)

    def test_06_add_product_to_cart(self):
        """Verifies increment in cart items when adding products."""
        self.driver.get(f"{self.BASE_URL}/product/1") # iPhone 15 details URL
        cart_page = CartPage(self.driver)
        
        cart_page.add_current_product_to_cart()
        
        # Verify count badge increases
        count = cart_page.get_cart_count()
        assert int(count) >= 1

    def test_07_complete_checkout_payment_flow(self):
        """Verifies full checkout billing address and credit card validation."""
        self.driver.get(f"{self.BASE_URL}/cart")
        cart_page = CartPage(self.driver)
        
        cart_page.proceed_to_checkout()
        
        # Fill Address Step
        cart_page.fill_shipping_address(
            address="123 QA St",
            zip_code="10001",
            phone="1234567890"
        )
        
        # Fill Credit Card Step
        cart_page.process_payment(
            card="4111111111111111", # Valid mock card passing Luhn test
            expiry="12/30",
            cvv="123"
        )
        
        # Verify Order ID generation and success screen display
        confirmation = cart_page.get_order_confirmation()
        assert "Order placed successfully" in confirmation
