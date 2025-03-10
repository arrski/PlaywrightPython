# Type: Page Class for login page
from playwright.sync_api import expect, Page

class LoginPage:

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.field_username = page.locator("[id=user-name]")
        self.field_password = page.locator("[data-test=\"password\"]")
        self.login_button = page.get_by_role("button", name="LOGIN")


    def load_page(self) -> None:
        self.page.goto(self.URL)

    def click_and_enter_user(self) -> None:
        self.field_username.click()
        self.field_username.fill("standard_user")

    def click_and_enter_pasword(self) -> None:
        self.field_password.click()
        self.field_password.fill("secret_sauce")

    def click_login_button(self) -> None:     
        self.login_button.click()