from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_action_class():
    """Test using Action Class for mouse and keyboard interactions."""
    print("Starting the test for Action Class interactions...")
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://blazedemo.com/")
        print("Opened Blaze Demo homepage.")
        time.sleep(2)

        # initialize ActionChains
        actions = ActionChains(driver)

        # hover over the "Find Flights" button
        print("Hovering over the 'Find Flights' button...")
        find_flights_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit']"))
        )
        actions.move_to_element(find_flights_button).perform()
        time.sleep(2)  # Delay to observe hover action

        # click the "find flights" button using ActionChains
        print("Clicking the 'Find Flights' button using ActionChains...")
        find_flights_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit']"))
        )
        actions.click(find_flights_button).perform()
        time.sleep(3)

        # re-find the element to avoid stale reference
        print("Double-clicking on a button (simulating)...")
        double_click_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit']"))
        )
        actions.double_click(double_click_button).perform()
        time.sleep(2)

        # right-click (context click)
        print("Right-clicking on an element (simulating)...")
        context_click_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit']"))
        )
        actions.context_click(context_click_button).perform()
        time.sleep(2)

        # drag-and-drop example
        print("Simulating drag-and-drop (if applicable)...")
        try:
            source_element = driver.find_element(By.ID, "draggable")  # Replace with actual ID
            target_element = driver.find_element(By.ID, "droppable")  # Replace with actual ID
            actions.drag_and_drop(source_element, target_element).perform()
            print("Drag-and-drop action performed.")
        except Exception as e:
            print("Drag-and-drop elements not found; skipping this part.")

    except Exception as e:
        print(f"Test encountered an error: {str(e)}")
    finally:
        print("Closing the browser...")
        driver.quit()


if __name__ == "__main__":
    test_action_class()
