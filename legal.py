from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BASE_URL = "https://zola.planning.nyc.gov/about"
INPUTELM_ID = "ember156"
UL_CLASSNAME = "lot-zoning-list"

def legalCheck(district):
    # Does't work, do .contains instead
    if district[:4] == "C6-5" or district[:4] == "C6-7" or district[:2] == "C7" or district[:2] == "C8" or district[:2] == "M1" or district[:2] == "M2" or district[:2] == "M3":
        return True
    return False

def bot(address):
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    elem = wait.until(EC.element_to_be_clickable((By.ID, INPUTELM_ID)))
    elem = driver.find_element_by_id(INPUTELM_ID)
    elem.send_keys(address)   
    driver.implicitly_wait(5)
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element_by_class_name("highlighted-result")
    elem.click()
    elems = driver.find_elements_by_xpath("//a[contains(@href, 'https://www1.nyc.gov/site/planning/zoning/districts-tools/')]")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "menu-text")))
    elems = driver.find_elements_by_xpath("//a[contains(@href, 'https://www1.nyc.gov/site/planning/zoning/districts-tools/')]")
    i = 0
    text = []
    while i < len(elems):
        text.append(elems[i].get_attribute("innerText"))
        i += 1
    return text

def main(address):
    text = bot(address)
    districts = [el.strip() for el in text if "R" in el or "M" in el or "C" in el]
    print(districts)
    return legalCheck(districts[-1])
print(main("66 W Broadway, New York, NY, USA"))



