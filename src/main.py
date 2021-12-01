from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time

from settings import DRIVER_PATH

URL = 'https://cav.receita.fazenda.gov.br/autenticacao/login'

def main():
    s = Service(DRIVER_PATH)
    options = Options()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options,
                              service=s)

    driver.set_page_load_timeout(5)

    try:
        driver.get(URL)
    except TimeoutException:
        driver.execute_script("window.stop();")

    button = driver.find_element(By.XPATH, "//div[@id='login-dados-certificado']/p[2]/input")

    time.sleep(0.25)
    button.click()
    time.sleep(10)

if __name__ == '__main__':
    main()
