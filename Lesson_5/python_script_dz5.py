from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_remove_elements():
  driver = webdriver.Chrome() 
  driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

  # Добавьте время для загрузки страницы
  time.sleep(2)

  # Увеличиваем время ожидания
  driver.implicitly_wait(10)

  # Ждем, пока кнопка "Add Element" станет кликабельной
  add_element_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > button"))
  ) 
  for _ in range(5):
    add_element_button.click()

  # Ждем, пока все элементы появятся на странице
  time.sleep(2)

  # Получаем все кнопки "Delete"
  delete_buttons = driver.find_elements(By.CSS_SELECTOR, "#elements > button")

  # Выводим размер списка
  print(f"Размер списка кнопок 'Delete': {len(delete_buttons)}")

  # Закрываем браузер
  driver.quit()

test_add_remove_elements()
