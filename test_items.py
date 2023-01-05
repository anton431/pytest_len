import time

def test_button_exist(browser):
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_elements(by="css selector", value="button.btn.btn-lg.btn-primary")
    assert button, 'button not exist'
    time.sleep(30)
