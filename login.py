from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# Use your saved Chrome profile
options.add_argument("--user-data-dir=chrome-profile")

driver = webdriver.Chrome(options=options)

driver.get("https://x.com/login")

print("Login manually and then close the browser")