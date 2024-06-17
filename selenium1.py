from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Get search topic from user input
search = input("Enter topic: ")
search = search.replace(' ', '+')

# Initialize the Chrome driver using WebDriver manager
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Construct the Google search URL
url = f"https://www.google.com/search?q={search}&start=0"

# Fetch the search results page
browser.get(url)

# Wait for the page to load (consider using explicit waits in real scenarios)
time.sleep(3)

# Optionally, you can perform additional actions on the results page
# For example, printing the titles of the search results
results = browser.find_elements(By.CSS_SELECTOR, 'h3')
for result in results:
    print(result.text)

# Close the browser
browser.quit()
