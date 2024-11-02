from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # Импортируем модуль time

# Запуск браузера
driver = webdriver.Chrome() 

# Переход на страницу
driver.get("http://uitestingplayground.com/classattr")

# Ожидание полной загрузки страницы
wait = WebDriverWait(driver, 10) 
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Поиск синей кнопки по CSS-классу и клик
blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
blue_button.click()

time.sleep(5) # Пауза в 5 секунд
# Закрытие браузера
driver.quit()
