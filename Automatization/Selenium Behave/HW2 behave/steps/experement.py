from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

 #================ GENERAL FUNCTIONS ==================#
  

#Откроем главную страницу в Chrome. Передадим в качестве аргумента адрес страницы.
@given('on Chrome website "{url}"')
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get(url)
    
#Откроем главную страницу в Edge. Передадим в качестве аргумента адрес страницы.    
@given('on Edge website "{url}"')
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
    
  
#==================== YAHOO =========================#
    
#Теперь введём запрос в Yahoo
@then("push into field text '{text}'")
def step(context, text):

    context.browser.find_element(By.XPATH, '//*[@id="ybar-sbq"]').send_keys(text)
    
      
#Теперь нажмем на кнопку "Найти" в Yahoo
@then("push button with text '{text}'")
def step(context, text):

    context.browser.find_element(By.XPATH, '//*[@id="ybar-search"]').click()

#Теперь нажмем на кнопку "Очистить" в Yahoo
@then("push Clear button with text '{text}'")
def step(context, text):

    context.browser.find_element(By.XPATH, '//*[@id="sbq-clear"]').click()

#Теперь введём Второй запрос в Yahoo
@then("push again into field text '{text}'")
def step(context, text):

    context.browser.find_element(By.XPATH, '//*[@id="yschsp"]').send_keys(text) 
    
#Теперь Второй раз нажмем на кнопку "Поиск", маленькую, в поисковой строке  Yahoo
@then("push Search little button with text '{text}'")
def step(context, text):

    context.browser.find_element(By.XPATH, '//*[@id="sf"]/label[2]/input').click()

    
    
 

 #===================== GOOGLE ============================#
 
#Теперь введём запрос в Google
@then("insert to field text '{text}'")
def step(context, text):

    context.browser.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(text)
    
#Теперь нажмём кнопку "Очистить" в Google
@then("push Clear button text '{text}'")
def step(context, text):

    context.browser.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[3]/div[1]/div').click()
    
#Теперь введём ВТОРОЙ запрос в Google
@then("insert again to field text '{text}'")
def step(context, text):

        context.browser.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(text)
    
#Теперь нажмем на кнопку "Поиск в Google"  ВТОРОЙ РАЗ
@then("push little Google Search button with text '{text}'")
def step(context, text):

    context.browser.find_element(By.CSS_SELECTOR, '[jsname="Tg7LZd"]').click()
  
#Теперь нажмем на кнопку "Поиск в Google"  
@then("push Google Search button with text '{text}'")
def step(context, text):

    context.browser.find_element(By.CSS_SELECTOR, '[name="btnK"]').click()
    
        
