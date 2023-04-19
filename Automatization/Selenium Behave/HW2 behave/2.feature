#Укажем что это за фича
Feature: Checking search Yahoo on Chrome
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Сheck some text in search results
#И используем наши шаги.
  Given on Chrome website "https://yahoo.com"
  Then push into field text 'beer'
  Then push button with text 'Найти'
  Then page include text 'Beer'
  Then push Clear button with text 'Clear'
  Then push again into field text 'coffee'
  Then push Search little button with text 'Search the web'
  Then page include text 'coffee'
