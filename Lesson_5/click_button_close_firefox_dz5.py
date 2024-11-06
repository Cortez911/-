from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

  # Запуск браузера
driver = webdriver.Firefox()

  # Переход на страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

  # Ожидание полной загрузки страницы
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body'))) 

  # Ожидание появления модального окна
wait = WebDriverWait(driver, 30)
modal_window = wait.until(EC.presence_of_element_located((By.ID, 'modal')))

print("Модальное окно найдено!") # Добавляем сообщение в консоль

  # Клик на кнопку "Close"
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p")))
close_button.click()

print("Кнопка 'Close' нажата!") # Добавляем сообщение в консоль

time.sleep(5) # Пауза в 5 секунд
  # Закрытие браузера
driver.quit()
