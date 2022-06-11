from selenium.webdriver.common.by import By
from selenium import webdriver
def just_join():
    driver = webdriver.Chrome()
    driver.get('https://justjoin.it/all/all/junior?q=QA@skill')
    elements = driver.find_elements(by=By.XPATH, value='//*[@id="root"]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div/a')
    links =[ element.get_attribute("href") for element in elements if element.get_attribute("href") is not None]       
    driver.close()
    return links