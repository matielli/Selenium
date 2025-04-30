from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

try:
    driver.get("https://formy-project.herokuapp.com/form")
    time.sleep(1)

    driver.find_element(By.ID, "first-name").send_keys("Ana")
    driver.find_element(By.ID, "last-name").send_keys("Silva")
    driver.find_element(By.ID, "job-title").send_keys("Analista de QA")
    driver.find_element(By.ID, "radio-button-2").click()
    driver.find_element(By.ID, "checkbox-2").click()

    Select(driver.find_element(By.ID, "select-menu")).select_by_visible_text("Europe")
    driver.find_element(By.XPATH, '//a[@class="btn btn-lg btn-primary"]').click()

    time.sleep(2)
    print("Formulário enviado com sucesso.")
    status = "Passou"
except Exception as e:
    print("Erro:", e)
    status = "Falhou"
finally:
    driver.quit()
