from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")    
    browser = webdriver.Chrome()
    browser.maximize_window()    
    browser.get('file:///C:/temp/QA/Git/My_HTML/Work/Selen/first.html')
    browser.delete_all_cookies()
    timer = browser.find_element(By.XPATH, '//*[@id="start"]').click()

    try:

        element = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    except:
        numb = browser.find_element(By.XPATH, '//*[@name="btn"]').click()
    try:
        elem = WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState").equals("complete"))

    except:
        # numb = browser.find_element(By.XPATH, '//*[@name="btn"]').click()  # Прекращает исполнение кода. не закрывая браузер, чтобы была возможность увидеть статус document.readyState -"complete", нужно только для отчёта.
        browser.quit()
        print('Test Is Successful!!')
main()