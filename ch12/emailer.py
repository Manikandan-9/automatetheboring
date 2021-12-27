import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

to_address = sys.argv[1]
subject = sys.argv[2]
content = sys.argv[3]

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?service=mail')

user_name=browser.find_element_by_name('identifier')
user_name.send_keys('mailid')
user_name.send_keys(Keys.ENTER)


password = browser.find_element_by_name('password')
password.send_keys('password')
password.send_keys(Keys.ENTER)


compose = browser.find_element_by_class_name('z0')
compose.click()



to = browser.find_element_by_name('to')
to.send_keys(to_address)


subjectel = browser.find_element_by_name('subjectbox')
subjectel.send_keys(subject)


subject.send_keys(Keys.TAB + content + Keys.TAB + Keys.ENTER)


browser.quit()