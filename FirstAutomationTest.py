from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get('https://www.neuralnine.com/')

driver.maximize_window()

# links = driver.find_element("xpath", "//a[@href]")
# for link in links:
#      if "Books" in link.get_attribute("innerHTML"):
#          link.click()
#          break

import random
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('C:\BrowserDrivers\chrome-win64')
# driver.get('http://www.google.com/')
#
# time.sleep(5)
# search_box = driver.find_element('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)
# driver.quit()
#
