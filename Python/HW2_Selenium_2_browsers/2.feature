
Feature: Проверка поиска Yahoo, Google в браузерах Chrome и Edge

Scenario: Поиск двух запросов подряд в Google через Chrome

  Given on Chrome website "https://www.google.com/"
  Then insert to field text 'beer'
  Then push Google Search button with text 'Поиск в Google'
  Then page include text 'Beer'
  Then push Clear button text 'Очистить'
  Then insert again to field text 'Вобла'
  Then push little Google Search button with text 'Поиск'
  Then page include text 'Вобла'


Scenario: Поиск двух запросов подряд в Yahoo через Edge

  Given on Edge website "https://yahoo.com"
  Then push into field text 'Сивушные масла'
  Then push button with text 'Найти'
  Then page include text 'Сивушные масла'
  Then push Clear button with text 'Clear'
  Then push again into field text 'белочка'
  Then push Search little button with text 'Search the web'
  Then page include text 'белочка'
  
Scenario: Поиск двух запросов подряд Yahoo через Chrome

  Given on Chrome website "https://yahoo.com"
  Then push into field text 'Ибн Баттута'
  Then push button with text 'Найти'
  Then page include text 'Ибн Баттута'
  Then push Clear button with text 'Clear'
  Then push again into field text 'Бактриан'
  Then push Search little button with text 'Search the web'
  Then page include text 'Бактриан'
  
Scenario: Поиск двух запросов подряд в Google через Edge

  Given on Edge website "https://www.google.com/"
  Then insert to field text 'драники'
  Then push Google Search button with text 'Поиск в Google'
  Then page include text 'драники'
  Then push Clear button text 'Очистить'
  Then insert again to field text 'Steak'
  Then push little Google Search button with text 'Поиск'
  Then page include text 'steak'
  
