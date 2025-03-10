#Type: Page Class for shop page
from playwright.sync_api import Page

class ShopPage:

    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator('//*[@id="add-to-cart-sauce-labs-backpack"]')
        self.go_to_cart_button = page.locator('//*[@id="shopping_cart_container"]/a')
        self.add_product_button = page.get_by_role('button', name='ADD TO CART')

    def add_backpack_to_cart(self) -> None:
        self.add_to_cart_button.click()

    def go_to_cart(self) -> None:
        self.go_to_cart_button.click()

    def add_items_to_cart(self, number_of_items: int) -> None:
        for i in range(number_of_items):
            self.add_product_button.nth(i).click()

