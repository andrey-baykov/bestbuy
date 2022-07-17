import pytest
import selenium.webdriver


@pytest.fixture
def browser():

    # Initialize WebDriver instance
    b = selenium.webdriver.Chrome()

    # Make its calls wait up to 10 seconds
    b.implicitly_wait(10)

    # Return the WebDriver for thr setup
    yield b

    # Quit thr WebDriver for the cleanup
    b.quit()
