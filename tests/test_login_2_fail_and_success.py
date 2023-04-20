from pages.login_page import LoginPage
import pytest


@pytest.mark.parametrize("all_users_test",
                         [("invaliduser1", "invalidpass1"), ("invaliduser2", "invalidpass2"), ("Admin", "admin123")])
def test_login_2_fail_and_success(driver, all_users_test):
    page = LoginPage(driver)
    page.visit_url()
    page.is_loginpage_displayed()
    page.login(all_users_test[0], all_users_test[1])
    if all_users_test[0] == "Admin":
        page.is_login_successfull()
    else:
        page.fail_login_message
