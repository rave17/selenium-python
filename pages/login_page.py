from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import get_url


# Clase base que contiene elementos que seran de uso frecuente en las pruebas
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.NAME, "username")
        self.password_textbox = (By.NAME, "password")
        self.login_button = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        self.fail_login_message = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")
        self.required_field_msg = (By.XPATH, "//span[contains(text(), 'Required field')]")

    def visit_url(self):
        url_to_test = get_url()
        self.driver.get(url_to_test)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_required_field_msg(self):
        try:
            requierd_message = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.required_field_msg))
            assert requierd_message.text == "Requierd"
            return True
        except:
            # código que se ejecuta si se produce la excepción
            print('Falta un dato requerido')
            return False

    def is_loginpage_displayed(self):
        try:
            # código que puede lanzar una excepción
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.login_button))
            print('pagina cargada')
            return True
        except:
            # código que se ejecuta si se produce la excepción
            print('No se cargo la pagina y produjo una excepcion')
            return False

    def is_login_successfull(self):
        try:
            login_message = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.driver.current_url))
            assert login_message in self.driver.current_url

            return True
        except:
            return False

    def is_login_failed(self):
        try:
            error_message = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.fail_login_message))
            assert error_message.text == "Invalid credentials"

            return True
        except:
            return False
