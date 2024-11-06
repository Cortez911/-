from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # Импортируем time

# Запуск браузера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Ожидание полной загрузки страницы
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Поиск кнопки по CSS селектору
blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary') 
blue_button.click()

time.sleep(5) # Пауза в 5 секунд
# Закрытие браузера
driver.quit()
