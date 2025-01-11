from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_select_class():
    print("Starting the test for Select Class interactions...")
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        driver.get("https://blazedemo.com/")
        print("Opened Blaze Demo homepage.")
        time.sleep(2)

        # locate dropdown elements for departure and destination cities
        print("Locating dropdowns for departure and destination cities...")
        departure_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "fromPort"))
        )
        destination_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "toPort"))
        )

        # use Select Class to interact with the dropdowns
        print("Selecting departure city: Boston...")
        departure_select = Select(departure_dropdown)
        departure_select.select_by_visible_text("Boston")
        time.sleep(1)

        print("Selecting destination city: London...")
        destination_select = Select(destination_dropdown)
        destination_select.select_by_visible_text("London")
        time.sleep(1)  # delay for clarity

        # verify the selected values
        selected_departure = departure_select.first_selected_option.text
        selected_destination = destination_select.first_selected_option.text

        if selected_departure != "Paris" or selected_destination != "Buenos Aires":
            raise Exception("Dropdown selections do not match the expected values.")

        print(f"Selected departure: {selected_departure}, Selected destination: {selected_destination}")

        # click on "find flights" button
        print("Submitting search with selected options...")
        find_flights_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        find_flights_button.click()

        print("Waiting for the search results page to load...")
        results_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )
        print(f"Search results title: {results_title.text}")

        if "Flights from Paris to Buenos Aires:" not in results_title.text:
            raise Exception("Search results title does not match the selected cities.")

        print("Search results successfully verified.")

    except Exception as e:
        print(f"Test encountered an error: {str(e)}")
    finally:
        print("Closing the browser...")
        driver.quit()


if __name__ == "__main__":
    test_select_class()
