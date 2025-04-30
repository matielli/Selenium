from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


start_time = datetime.now()
print(f"Início do teste: {start_time}")
driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

  
    start_button = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    start_button.click()

 
    wait = WebDriverWait(driver, 10)
    result = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    assert "Hello World!" in result.text
    print("Texto carregado com sucesso.")

    status = "Passou"
except Exception as e:
    print(f"Erro: {e}")
    status = "Falhou"
finally:
    end_time = datetime.now()
    print(f"Fim do teste: {end_time}")
    print(f"Tempo de espera: {end_time - start_time}")
    driver.quit()
