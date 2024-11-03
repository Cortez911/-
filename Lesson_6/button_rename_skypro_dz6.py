from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера Chrome
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/textinput")

# Ожидание полной загрузки страницы
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Поиск поля ввода и ввод текста
input_field = wait.until(EC.presence_of_element_located((By.ID, 'newButtonName')))
input_field.send_keys("SkyPro")

# Поиск синей кнопки и клик
blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
blue_button.click()

# Ожидание появления переименованной кнопки
renamed_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='SkyPro']")))

# Получение текста кнопки и вывод в консоль
print(renamed_button.text)

# Закрытие браузера
driver.quit()
