import pytest
from selenium.common.exceptions import WebDriverException
from utils.config_reader import get_users_test
from config.driver import get_driver


# El siguiente fixture utiliza el fixture "driver" y envi "driver.py"
# para inicializar la página de inicio de sesión en cada prueba.
@pytest.fixture(params=['chrome'], scope='module')
def driver(request):
    browser = request.param
    driver_to_use = get_driver(browser)
    yield driver_to_use
    try:
        driver_to_use.quit()
    except WebDriverException:
        pass


# Este fixture puede utilizarse para realizar pruebas repetitivas con usuarios
# utilizando diferentes credenciales de usuario.
@pytest.fixture(params=get_users_test())
def all_users_test():
    data_test = get_users_test()
    return data_test["valid_users"] + data_test["invalid_users"]


# Este fixture puede utilizarse para realizar acciones de inicio de sesión en la página de login
# utilizando credenciales de usuario validas.
@pytest.fixture(scope="session")
def valid_users():
    data_test = get_users_test()
    valid_users_data = data_test["valid_users"]
    return valid_users_data


# Este fixture puede utilizarse para realizar acciones de inicio de sesión en la página de login
# utilizando credenciales de usuario invalidas.
@pytest.fixture(scope="session")
def invalid_users():
    data_test = get_users_test()
    invalid_users_data = data_test["invalid_users"]
    return invalid_users_data
