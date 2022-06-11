
from selenium.webdriver.common.by import By
from selenium import webdriver
def nofluffjobs():
    driver = webdriver.Chrome()
    driver.get('https://nofluffjobs.com/pl/?criteria=seniority%3Dtrainee,junior%20jobLanguage%3Dpl%20keyword%3Dtester,qa&page=1')
    elements = driver.find_elements(by=By.CLASS_NAME, value='posting-list-item')
    links =[ element.get_attribute("href") for element in elements if element.get_attribute("href") is not None]            
    driver.close()
    return links