from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера Chrome
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/ajax")

# Ожидание полной загрузки страницы
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Поиск синей кнопки и клик
blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#ajaxButton')))
blue_button.click()

# Ожидание появления зеленой плашки
green_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#content > p')))

# Получение текста из зеленой плашки и вывод в консоль
print(green_text.text)

# Закрытие браузера
driver.quit()
