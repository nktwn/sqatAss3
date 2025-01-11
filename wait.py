from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


def setup_driver():
    """Initialize the WebDriver and return the instance."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Driver initialized and browser window maximized.")
    return driver


def select_city(driver, element_name, city_name):
    """Select a city from a dropdown menu by visible text."""
    dropdown = driver.find_element(By.NAME, element_name)
    Select(dropdown).select_by_visible_text(city_name)
    print(f"Selected {city_name} in dropdown: {element_name}")


def test_waits():
    """Test implicit, explicit, and fluent waits."""
    print("Starting the test for implicit, explicit, and fluent wait...")
    driver = setup_driver()

    try:
        driver.get("https://blazedemo.com/")
        print("Opened Blaze Demo homepage.")

        # implicit Wait
        print("Setting implicit wait of 10 seconds...")
        driver.implicitly_wait(10)  # Set implicit wait

        # select departure and destination cities
        select_city(driver, "fromPort", "Paris")
        select_city(driver, "toPort", "Buenos Aires")
        print("Selected departure and destination cities.")

        # click on "Find Flights" button
        find_flights_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        find_flights_button.click()
        print("Searching for flights...")

        # explicit Wait
        print("Using explicit wait to wait for the search results page...")
        wait = WebDriverWait(driver, 10)
        results_title = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )
        print(f"Results page loaded. Title: {results_title.text}")

        # verify the results page title
        if "Flights from Paris to Buenos Aires:" not in results_title.text:
            raise Exception("Search results title does not match expected.")
        print("Search results title verified.")

        # fluent Wait
        print("Using fluent wait to wait for the first flight selection button...")
        fluent_wait = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[TimeoutException])
        choose_flight_button = fluent_wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))
        )
        print("Flight selection button found. Clicking the button...")
        choose_flight_button.click()

        # verify successful navigation to the booking form
        print("Waiting for the booking form to load...")
        booking_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        if booking_form:
            print("Booking form successfully loaded.")
        else:
            raise Exception("Booking form failed to load.")

    except Exception as e:
        print(f"Test encountered an error: {str(e)}")
    finally:
        print("Closing the browser...")
        driver.quit()


if __name__ == "__main__":
    test_waits()
