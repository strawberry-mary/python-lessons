import time

def test_user_add_item_in_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element_by_class_name("btn-primary")
    button_name=button.text
    assert button_name is not None
    time.sleep(5)    


