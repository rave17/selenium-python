import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("invalid_users", ["users"], indirect=True)
def test_login_3_attempts(driver, invalid_users):
    page = LoginPage(driver)
    for i in range(3):
        page.visit_url()
        page.is_loginpage_displayed()
        page.login(invalid_users[0]["username"], invalid_users[1]["password"])
        page.is_loginpage_displayed()

    page.visit_url()
    page.is_loginpage_displayed()
    page.enter_username(invalid_users[0]["username"])
    page.click_login()
    page.is_loginpage_displayed()
    page.get_required_field_msg()