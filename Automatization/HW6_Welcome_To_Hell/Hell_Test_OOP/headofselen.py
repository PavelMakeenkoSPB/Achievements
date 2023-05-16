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
find_element = browser.find_element
find_elements = browser.find_elements