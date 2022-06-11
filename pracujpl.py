from selenium.webdriver.common.by import By
from selenium import webdriver
def pracuj():
    driver = webdriver.Chrome()
    driver.get('https://www.pracuj.pl/praca/software%20tester;kw?et=1')
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="gp-cookie-agreements"]/div/div/div[1]/div[3]/button').click()
    except:
        print("no agreement needed")
    elements = driver.find_elements(by=By.CLASS_NAME, value='offer-details__title-link')
    links =[ element.get_attribute("href") for element in elements if element.get_attribute("href") is not None]               
    driver.close()
    return links