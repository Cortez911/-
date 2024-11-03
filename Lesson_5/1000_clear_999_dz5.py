from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Запуск браузера
driver = webdriver.Firefox()

# Переход на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Ожидание полной загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Поиск поля ввода
input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))

# Ввод текста "1000"
input_field.send_keys("1000")
print("Введено 1000") # Добавляем сообщение в консоль
time.sleep(5)

# Очистка поля
input_field.clear()
print("Поле очищено") # Добавляем сообщение в консоль 
time.sleep(0.5) 

# Ввод текста "999"
input_field.send_keys("999")
print("Введено 999") # Добавляем сообщение в консоль
time.sleep(5)

time.sleep(2)
# Закрытие браузера
driver.quit()
