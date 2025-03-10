# Type: Page Class for cart page
from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.quantity = page.locator('//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[1]')


