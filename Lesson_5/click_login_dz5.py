from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Запуск браузера
driver = webdriver.Firefox()

# Переход на страницу
driver.get("http://the-internet.herokuapp.com/login")

# Ожидание полной загрузки страницы
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Поиск поля username
username_field = wait.until(EC.presence_of_element_located((By.ID, 'username')))
username_field.send_keys("tomsmith")
print("Введен логин: tomsmith")
time.sleep(2)

# Поиск поля password
password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
password_field.send_keys("SuperSecretPassword!")
print("Введен пароль: SuperSecretPassword!")
time.sleep(2)

# Поиск кнопки Login и клик
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login > button > i")))
login_button.click()
print("Вход выполнен")
time.sleep(2)

time.sleep(2)
# Закрытие браузера
driver.quit()
