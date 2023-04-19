Feature: Проверка результатов поиска "World of tanks" через Google в браузерах Chrome и Edge

Scenario: Поиск запроса "World of tanks" в Google через Chrome

  Given on Chrome website 'https://www.google.com/'
  When insert to field text 'World of tanks'
  When push Google Search button with text 'Поиск в Google'
  When type into search field "World of "
  When the number of options in the drop-down list is 10
  When first option is "World of tanks" with img and text
  When list of adjustments is 5
  Then page include text 'World of tanks'

  
Scenario: Поиск запроса "World of tanks" в Google через Edge

  Given on Edge website 'https://www.google.com/'
  When insert to field text 'World of tanks'
  When push Google Search button with text 'Поиск в Google'
  When type into search field "World of "
  When the number of options in the drop-down list is 10
  When first option is "World of tanks" with img and text
  When list of adjustments is 5
  Then page include text 'World of tanks'  