from selenium import webdriver

# Initialize the driver
driver = webdriver.Firefox()

# Load the URL
url = "https://www.jhv.cz"
driver.get(url)

# Take the screenshot
driver.save_screenshot("screenshot.png")

# Quit the driver
driver.quit()