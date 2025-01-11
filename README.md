# Selenium Advanced Testing Assignment 3

## Overview
This project demonstrates advanced Selenium WebDriver techniques using the Blaze Demo flight booking application. The key objectives are:
1. Implementing wait strategies (implicit, explicit, and fluent waits).
2. Using ActionChains for complex user interactions.
3. Utilizing the Select class for dropdown handling.
4. Creating a structured test report.


### Wait Strategies (wait.py)

Objective:
To showcase implicit, explicit, and fluent waits for handling synchronization.

How It Works:
- Implicit Wait: Sets a global wait time for element loading.
- Explicit Wait: Waits specifically for the search results' title.
- Fluent Wait: Continuously checks for a clickable button.

Run Command: `python wait.py`


### Action Chains (action_class.py)

Objective:
To perform advanced user interactions like hovering, clicking, double-clicking, and right-clicking.

How It Works:
- Simulates mouse and keyboard actions using ActionChains.
- Includes a drag-and-drop simulation (if applicable).

Run Command: `python action_class.py`


### Select Class (select_class.py)

Objective: 
To handle dropdowns for selecting departure and destination cities.

How It Works: 
- Uses the Select class to select dropdown options.
- Verifies the selected values and search results page title.

Run Command: `python select_class.py`