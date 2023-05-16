from headofselen import *

class Visible():

    def SomeElementsAreVisible(self):
               
        # Проверка видимости заголовка страницы

        header = find_element(By.XPATH, '//h1[contains(.,"Семь Кругов Ада")]').is_displayed()
        print("OK - Заглавие страницы отображается")

        # Проверка наличия фото Жукова
        serega = find_element(By.XPATH, '//tr[5]/td[2]').is_displayed()
        print("OK - Сергей Жуков в Аду")

        # Проверка  количества блоков приветсвенного текста
        amountOfTextBlocks = find_elements(By.XPATH, '//div[1]/p')
        assert len(amountOfTextBlocks) == 6
        print("OK - Количество блоков приветсвенного текста: 6")

        # Проверка количества круглых значков
        numberOfSights = find_elements(By.XPATH, '//a/img')
        assert len(numberOfSights) == 4
        print("OK - Количество круглых значков: 4")

        # Проверка количества картинок в таблице Услуг
        amountOfService = find_elements(By.XPATH, '//tbody[2]/tr/td/img')
        assert len(amountOfService) == 7
        print("OK - Количество картинок услуг: 7")

        # Проверка количества картинок на странице
        numberOfImg = find_elements(By.XPATH, '//img')
        assert len(numberOfImg) == 23
        print("ОK - Количество картинок: 23")

    def QuitBrowser(self):
        browser.quit()
        print("Тест завершён успешно!")    


class Iframe():
    
    def IFrameWorking(self):
        #Функционирование элемента slider и выставленеи значения 860
        donate = find_element(By.XPATH, '//input[@name="amountMoney"]')
        actions = ActionChains(browser)
        actions.click_and_hold(donate).move_by_offset(133, 0).release().perform()
        print("ОК - Значение выставляется ползунком")
    
        #Нажатие кнопки Поддать дров
        pushDonate = find_element(By.XPATH, '//input[@name="isubmit"]').click()
        time.sleep(5)
        print("ОК - Кнопка 'Поддать дров' работает")


class AnketaForm():

    def AnketaChecking(self):
        #Ввод текста в Анкету
        insertName = find_element(By.XPATH, '//input[@name="hisname"]').send_keys("Квазиморд Витальевич")
        insertAge = find_element(By.XPATH, '//input[@name="age"]').send_keys(98)
        print("ОК - Поля ввода анкетных данных функционируют")
    
        #Проверка активности чек-бокса Шоу и активация другого чек-бокса Орешки
        checkedChekbox = find_element(By.XPATH, '//p/input[3]').is_selected()
        selectCheckbox = find_element(By.XPATH, '//p/input[4]').click()
        print("ОК - Чекбоксы активны и кликабельны")
    
        # Выбор опции Шаманист из выпадающего списка богов
        godChoising = find_element(By.XPATH, '//select[@name="god"]')
        select = Select(godChoising)
        select.select_by_visible_text("Шаманист")
        print("ОК - Бога можно выбрать в меню")
    
        #Ввод текста в текстовое поле О госте
        typeText = find_element(By.XPATH, '//textarea').send_keys("Трёшка на Парнасе...я наследник, а он всё никак!!! ЫЫыы!!\n")
    
        #Нажатие кнопки Знайте же
        pushKnowThis = find_element(By.XPATH, '//input[@name="getinfo"]').click()
        print("ОК - Кнопка 'Знайте же' работает")

class TextForm():

    def TextAssert(self):
        # Проверка наличия текста До встречи в Аду, пьяницы! в словах льва
        lionsTale = find_element(By.XPATH, '//td[contains(text(), "пьяницы")]')
        textLion = lionsTale.text
        assert "До встречи в Аду, пьяницы!" in textLion
        print('ОК - Лев не врёт')
    
        # Работа фрейма видеоплеера
        videoFrame = find_element(By.TAG_NAME, "iframe")
        actions.move_to_element(videoFrame)
        actions.perform()
        browser.switch_to.frame(videoFrame)
        playMovie = find_element(By.CSS_SELECTOR, '.ytp-large-play-button').click()
        time.sleep(11)
        pauseMovie = find_element(By.CSS_SELECTOR, '.ytp-play-button').click()
        browser.switch_to.default_content()
        print("ОК - Плеер работает")
        
class LinkCheck():

    def LinkChecking(self):
        # Поиск и переход по ссылкам Круглых Значков
        sevenSinght = find_element(By.XPATH, '//img[@alt="seven"]').click()
        roundSight = find_element(By.XPATH, '//img[@alt="round"]').click()
        adaSight = find_element(By.XPATH, '//img[@alt="Ада"]').click()
        parrotSight = find_element(By.XPATH, '//img[@alt="popugay"]').click()
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
