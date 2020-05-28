from selenium import webdriver
import sys

driver = webdriver.Firefox()
driver.get('https://www.amazon.ca/')
search_term = sys.argv[1]

searchbox = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')

searchbox.send_keys(search_term)

searchButton = driver.find_element_by_xpath(
	'/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')

searchButton.click()