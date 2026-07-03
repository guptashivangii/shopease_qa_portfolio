import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup_driver(request):
    """
    Setup driver fixture that instantiates Chrome WebDriver.
    Runs headless in CI systems.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode for clean execution
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # In standard execution environments, chromedriver should be on the system PATH.
    # If not on PATH, specify executable_path.
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    
    # Pass driver instance to requesting test class
    request.cls.driver = driver
    
    yield driver
    
    driver.quit()
