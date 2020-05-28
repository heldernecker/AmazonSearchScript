from selenium import webdriver
import sys

search_term = ""

try:
	search_term = sys.argv[1]
except:
	while not search_term:
		print("Please enter a term to be searched: ")
		search_term = input()

driver = webdriver.Firefox()
driver.get('https://www.amazon.ca/')

searchbox = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbox.send_keys(search_term)

searchButton = driver.find_element_by_xpath(
	'/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')
searchButton.click()