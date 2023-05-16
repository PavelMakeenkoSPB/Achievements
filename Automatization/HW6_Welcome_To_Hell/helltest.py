import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
actions = ActionChains(browser)
#browser.set_window_size(800, 600)
browser.maximize_window()    
browser.get('https://resortofhelling.netlify.app/')
original_window = browser.current_window_handle


def SomeElementsAreVisible():

    # Проверка видимости заголовка страницы

    header = browser.find_element(By.XPATH, '//h1[contains(.,"Семь Кругов Ада")]').is_displayed()
    print("OK - Заглавие страницы отображается")

    # Проверка наличия фото Жукова
    serega = browser.find_element(By.XPATH, '//tr[5]/td[2]').is_displayed()
    print("OK - Сергей Жуков в Аду")

    #Проверка  количества блоков приветсвенного текста
    amountOfTextBlocks = browser.find_elements(By.XPATH, '//div[1]/p')
    assert len(amountOfTextBlocks) == 6
    print("OK - Количество блоков приветсвенного текста: 6")
    
    #Проверка количества круглых значков
    numberOfSights = browser.find_elements(By.XPATH, '//a/img')
    assert len(numberOfSights) == 4
    print("OK - Количество круглых значков: 4")

    #Проверка количества картинок в таблице Услуг
    amountOfService = browser.find_elements(By.XPATH, '//tbody[2]/tr/td/img')
    assert len(amountOfService) == 7
    print("OK - Количество картинок услуг: 7")

    #Проверка количества картинок на странице
    numberOfImg = browser.find_elements(By.XPATH, '//img')
    assert len(numberOfImg) == 23
    print("ОK - Количество картинок: 23")

def IFrameWorking():
    #Функционирование элемента slider и выставленеи значения 860
    donate = browser.find_element(By.XPATH, '//input[@name="amountMoney"]')
    actions = ActionChains(browser)
    actions.click_and_hold(donate).move_by_offset(133, 0).release().perform()
    print("ОК - Значение выставляется ползунком")

    #Нажатие кнопки Поддать дров
    pushDonate = browser.find_element(By.XPATH, '//input[@name="isubmit"]').click()
    time.sleep(5)
    print("ОК - Кнопка 'Поддать дров' работает")

def AnketaChecking():
    #Ввод текста в Анкету
    insertName = browser.find_element(By.XPATH, '//input[@name="hisname"]').send_keys("Квазиморд Витальевич")
    insertAge = browser.find_element(By.XPATH, '//input[@name="age"]').send_keys(98)
    print("ОК - Поля ввода анкетных данных функионируют")

    #Проверка активности чек-бокса Шоу и активация другого чек-бокса Орешки
    checkedChekbox = browser.find_element(By.XPATH, '//p/input[3]').is_selected()
    selectCheckbox = browser.find_element(By.XPATH, '//p/input[4]').click()
    print("ОК - Чекбоксы активны и кликабельны")

    # Выбор опции Шаманист из выпадающего списка богов
    godChoising = browser.find_element(By.XPATH, '//select[@name="god"]')
    select = Select(godChoising)
    select.select_by_visible_text("Шаманист")
    print("ОК - Бога можно выбрать в меню")

    #Ввод текста в текстовое поле О госте
    typeText = browser.find_element(By.XPATH, '//textarea').send_keys("Трёшка на Парнасе...я наследник, а он всё никак!!! ЫЫыы!!\n")

    #Нажатие кнопки Знайте же
    pushKnowThis = browser.find_element(By.XPATH, '//input[@name="getinfo"]').click()
    print("ОК - Кнопка 'Знайте же' работает")

def TextAssert():
    # Проверка наличия текста До встречи в Аду, пьяницы! в словах льва
    lionsTale = browser.find_element(By.XPATH, '//td[contains(text(), "пьяницы")]')
    textLion = lionsTale.text
    assert "До встречи в Аду, пьяницы!" in textLion
    print('ОК - Лев не врёт')

    # Работа фрейма видеоплеера
    videoFrame = browser.find_element(By.TAG_NAME, "iframe")
    actions.move_to_element(videoFrame)
    actions.perform()
    browser.switch_to.frame(videoFrame)
    playMovie = browser.find_element(By.CSS_SELECTOR, '.ytp-large-play-button').click()
    time.sleep(11)
    pauseMovie = browser.find_element(By.CSS_SELECTOR, '.ytp-play-button').click()
    browser.switch_to.default_content()
    print("ОК - Плеер работает")

def LinkChecking():
    # Поиск и переход по ссылкам Круглых Значков
    sevenSinght = browser.find_element(By.XPATH, '//img[@alt="seven"]').click()
    roundSight = browser.find_element(By.XPATH, '//img[@alt="round"]').click()
    adaSight = browser.find_element(By.XPATH, '//img[@alt="Ада"]').click()
    parrotSight = browser.find_element(By.XPATH, '//img[@alt="popugay"]').click()
    print("ОК - Переход по 4 ссылкам")

    # Проверка количества открытых вкладок по ссылкам (их 5)
    pages = WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(5))
    print(pages, "- Были открыты 5 вкладок")

    # Цикл для закрытия четырёх новых вкладок
    time.sleep(2)
    i = 1
    k = 1
    for k in range(1, 5):
        for i in range(1, 2):
            window_after = browser.window_handles[i]
            browser.switch_to.window(window_after)
            browser.close()
    print("OK - Были закрыты 4 вкладки")
            
    # Переключение на начальную вкладку
    browser.switch_to.window(original_window)

def QuitBrowser():
    browser.quit()
    print("Тест завершён успешно!")

def Run():
    SomeElementsAreVisible()
    IFrameWorking()
    AnketaChecking()
    TextAssert()
    LinkChecking()
    QuitBrowser()
    
Run()


