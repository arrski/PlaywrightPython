from playwright.sync_api import expect, Page
from pages.login import LoginPage
from pages.shop import ShopPage
from pages.cart import CartPage
import re, logging

#player can log in with valid credentials
def test_player_can_log_in(page: Page) -> None:
    login_page = LoginPage(page)
    
    # sauce page is loaded
    login_page.load_page()

    # user and password are entered
    login_page.click_and_enter_user()
    login_page.click_and_enter_pasword()

    # login button is clicked
    login_page.click_login_button()

#player can add item to cart after logging in
def test_player_add_item(page: Page) -> None:
    login_page = LoginPage(page)
    shop_page = ShopPage(page)
    cart_page = CartPage(page)
    # sauce page is loaded
    login_page.load_page()
    # user and password are entered
    login_page.click_and_enter_user()
    login_page.click_and_enter_pasword()
    # login button is clicked
    login_page.click_login_button()
    
    expect(shop_page.add_to_cart_button).to_be_visible()
    shop_page.add_backpack_to_cart()
    shop_page.go_to_cart()
  
    expect(page.get_by_text("Your Cart")).to_have_count(1)
    expect(cart_page.quantity).to_have_attribute("class", re.compile(r"cart_quantity"))
    items_in_a_cart = cart_page.quantity.inner_text()
    assert items_in_a_cart == "1"
    number_of_items = cart_page.quantity.all_text_contents()
    assert len(number_of_items) > 0
    assert number_of_items[0] == "1"

    logging.info(f"Items in a cart: {items_in_a_cart}")







