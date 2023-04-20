import pytest

from pages.login_page import LoginPage


@pytest.mark.positive
@pytest.mark.parametrize("valid_users", ["users"], indirect=True)
def test_login_success(driver, valid_users):
    page = LoginPage(driver)
    page.visit_url()
    page.is_loginpage_displayed()
    # La función current_url del objeto driver de Selenium devuelve la URL actual de la página que está abierta en el
    # navegador. La aserción assert "dashboard" in driver.current_url verifica que la cadena "dashboard" está
    # incluida en la URL actual
    page.login(valid_users[0]["username"], valid_users[0]["password"])
    page.is_login_successfull()

