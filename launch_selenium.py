from selenium import webdriver
driver = webdriver.Chrome()

executor_url = driver.command_executor._url
session_id = driver.session_id

print (session_id)
print (executor_url)

driver.get("http://tarunlalwani.com")