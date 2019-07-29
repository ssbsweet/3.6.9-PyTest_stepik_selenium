def test_check_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.implicitly_wait(2)
    browser.get(link)
    basket_button_1 = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert basket_button_1
