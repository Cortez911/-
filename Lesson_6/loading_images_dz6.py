from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера Chrome
driver = webdriver.Chrome()

# Открываем сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждем, пока все изображения загрузятся
WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "img")))

# Находим все изображения
images = driver.find_elements(By.TAG_NAME, "img")

# Проверяем, есть ли на странице изображения
if len(images) >= 3:
  # Получаем значение атрибута src у 3-го изображения
  third_image = images[2]
  src_value = third_image.get_attribute("src")
  # Выводим значение в консоль
  print(src_value)

# Закрываем браузер
driver.quit()
