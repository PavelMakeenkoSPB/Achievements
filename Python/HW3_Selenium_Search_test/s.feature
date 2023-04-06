
Feature: Проверка результатов поиска "Бернский зенненхунд" через Google в браузерах Chrome и Edge

Scenario: Поиск запроса 'Бернский зенненхунд' в Google через Chrome

  Given on Chrome website "https://www.google.com/"
  When insert to field text 'Бернский зенненхунд'
  When push Google Search button with text 'Поиск в Google'
  When counter of search contains number of results
  When number of search results per page is 9
  When all of 4 images are displayed in results correctly
  Then page include text 'Бернский зенненхунд'
  
Scenario: Поиск запроса 'Бернский зенненхунд' в Google через Edge

  Given on Chrome website "https://www.google.com/"
  When insert to field text 'Бернский зенненхунд'
  When push Google Search button with text 'Поиск в Google'
  When counter of search contains number of results
  When number of search results per page is 9
  When all of 4 images are displayed in results correctly
  Then page include text 'Бернский зенненхунд'







  
