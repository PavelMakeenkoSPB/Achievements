Feature: Checking Google search  on Chrome
 
Scenario: Сheck some text in search results
 
  Given on Chrome website "https://www.google.com/"
  Then insert to field text 'beer'
  Then push Google Search button with text 'Поиск в Google'
  Then page include text 'Beer'
  Then push Clear button text 'Очистить'
  Then insert again to field text 'Масло'
  Then push little Google Search button with text 'Поиск'
  Then page include text 'Масло'