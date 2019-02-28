

from selenium import webdriver

driver = webdriver.Chrome('/Users/hongwei/Downloads/installs/chromedriver')
driver.fullscreen_window()
driver.get('https://www.baidu.com')