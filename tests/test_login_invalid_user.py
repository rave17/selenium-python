import pytest
from pages.login_page import LoginPage


@pytest.mark.negative
@pytest.mark.parametrize("invalid_users", ["users"], indirect=True)
def test_failed_invalid_user(driver, invalid_users):
    page = LoginPage(driver)
    page.visit_url()
    page.is_loginpage_displayed()
    page.login(invalid_users[0]["username"], invalid_users[0]["password"])
    page.is_login_failed()
