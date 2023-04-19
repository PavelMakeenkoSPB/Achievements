from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

 #=================== GENERAL FUNCTIONS ==================#
  
#Откроем главную страницу в Chrome. Передадим в качестве аргумента адрес страницы.
@given("on Chrome website '{url}'")
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    chrome_options = Options()
    
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get(url)
    
    
#Откроем главную страницу в Edge. Передадим в качестве аргумента адрес страницы.    
@given("on Edge website '{url}'")
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Edge()
    context.browser.maximize_window()
    context.browser.get(url)
 
 
#Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element(By.XPATH,'//*[contains(text(), "%s")]' % text)
    
  
 #====================== GOOGLE ===========================#
 
 #Теперь введём запрос в Google
@when("insert to field text '{text}'")
def step(context, text):
    context.browser.implicitly_wait(4)
    context.browser.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(text)
    
  
#Теперь нажмем на кнопку "Поиск в Google"  
@when("push Google Search button with text '{text}'")
def step(context, text):
    context.browser.find_element(By.CSS_SELECTOR, '[name="btnK"]').click()
   
     
# =======================  WORLD OF =========================# 

# Вводим текст в поисковую строку, чтобы получить выпадающий список
@when ('type into search field "{text}"')
def step(context, text):
    context.browser.find_element(By.CSS_SELECTOR, '[name="q"]').clear()
    context.browser.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(text)
    
    
# Ищем количество элементов выпадающего списка строки поиска  
@when ('the number of options in the drop-down list is 10')
def step(context):
    OptionsInList = context.browser.find_elements(By.XPATH,'//div[@class="lnnVSe" and @role="option" and @aria-description]')
    
    assert int(len(OptionsInList)) == 10


# Проверяем наличие в первом пункте выпадающего меню текста, картинки и подсказки
@when ('first option is "World of tanks" with img and text')
def step(context):
    HeadTextOnFirst = context.browser.find_element(By.XPATH,'(//span[contains(text(), "world of tanks")])[1]').is_displayed()
    ImageOnfirst = context.browser.find_element(By.XPATH,'(//div[contains(@class, "sbic")])[1]').is_displayed()
    SmallTextOnFirst =  context.browser.find_element(By.XPATH, "(//*[contains(text(), 'World of — Серия видеоигр')])[1]").is_displayed()

    assert HeadTextOnFirst == True and ImageOnfirst == True and SmallTextOnFirst == True
  
  
# Проверяем количество корректировочных пунктов выпадающего меню  
@when('list of adjustments is 5')
def step(context):
    ListOfAdjustments = context.browser.find_elements(By.XPATH,'//div[@class="sbic sb43"]')
    
    assert int(len(ListOfAdjustments)) == 5


