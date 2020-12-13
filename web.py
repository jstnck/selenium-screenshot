from selenium.webdriver import Firefox
#driver = Firefox(executable_path='./geckodriver')

print("set driver")
gecko_path = "/selenium/geckodriver"
log_path = "/selenium/logs/geckodriver.log"

driver = Firefox(executable_path=gecko_path, service_log_path=log_path)

print("driver.get")
driver.get("https://www.selenium.dev")

driver.save_screenshot("./data/screenshot1.png")

print(str(driver.title))
print(str(driver.current_window_handle))

driver.get("https://www.wired.com")
driver.save_screenshot("./data/screenshot2.png")

driver.back()