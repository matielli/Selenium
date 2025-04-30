from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)

   
    product = driver.find_element(By.XPATH, '//a[contains(text(),"Samsung galaxy s6")]')
    product.click()

   
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[text()="Add to cart"]'))
    ).click()

   
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

  
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//button[text()="Place Order"]').click()

    # Preencher dados
    driver.find_element(By.ID, "name").send_keys("João Teste")
    driver.find_element(By.ID, "country").send_keys("Brasil")
    driver.find_element(By.ID, "city").send_keys("São Paulo")
    driver.find_element(By.ID, "card").send_keys("1234123412341234")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2025")

    driver.find_element(By.XPATH, '//button[text()="Purchase"]').click()

    confirmation = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert"))
    )
    print("Confirmação de compra:", confirmation.text)

    status = "Passou"
except Exception as e:
    print("Erro:", e)
    status = "Falhou"
finally:
    time.sleep(3)
    driver.quit()
