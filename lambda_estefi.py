import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key
print(username)
print(access_key)

class FirstSampleTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
            'LT:Options': {
                "build": "Python Demo",  # Change your build name here
                "name": "Python Demo Test",  # Change your test name here
                "platformName": "Windows 11",
                "selenium_version": "4.0.0",
                "console": 'true',  # Enable or disable console logs
                "network": 'true',  # Enable or disable network logs
                #Enable Smart UI Project
                #"smartUI.project": "<Project Name>"
            },
            "browserName": "firefox",
            "browserVersion": "latest",
        }

        # Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
        # Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
        # Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
        # Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot 
        # Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/

        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities=desired_caps)

# tearDown runs after each test case


    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_demo_site(self):

        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print('Loading URL')
        driver.get("https://estandar-qa.sigea.cl")
        time.sleep(5)

        # Inicio de sesion
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Usuario']").send_keys(Usuario) 
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Contraseña']").send_keys(Clave)
        time.sleep(2)
        driver.find_element(By.ID, 'submit').click()
        time.sleep(10)

        # Ingresar al dominio (central hidráulica)

        driver.find_element(By.XPATH, '//*[@id="header"]/header/div[3]/ul[3]/li[2]').click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "#dominio_1 > i").click()
        time.sleep(5)

        # Ingresar a compromisos

        driver.find_element(By.ID, "menu2").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#submenu2 > li:nth-child(2) > a > div.ng-binding').click()
        time.sleep(5)

        # Descargar compromisos

        driver.find_element(By.CSS_SELECTOR, 'a[data-i18n="RCAs"]').click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, 'button[data-ng-click="descargaCompromisosExcel()"]').click()
        time.sleep(25)

        hoy = time.strftime("%d%m%Y")
        contenido = os.listdir('.\\Descarga\\')
        assert("Compromisos_RCA_" + hoy + ".xlsx" in contenido)

        time.sleep(5)
        driver.quit()



if __name__ == "__main__":
    unittest.main()
