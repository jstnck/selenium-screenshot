from selenium.webdriver import Firefox

gecko_path = "/selenium/geckodriver"
log_path = "/selenium/logs/geckodriver.log"
driver = Firefox(executable_path=gecko_path, service_log_path=log_path)

driver.get("https://www.basketball-reference.com/boxscores/202010110MIA.html")

driver.save_screenshot("./data/lalmia.png")

print(str(driver.title))
print(str(driver.current_window_handle))

