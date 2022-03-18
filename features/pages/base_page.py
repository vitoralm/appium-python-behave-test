class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator):
        return self.driver.find_elements(by=locator[0], value=locator[1])

    def find_element(self, locator):
        return self.driver.find_element(by=locator[0], value=locator[1])

    def click_on_element(self, locator):
        element = self.driver.find_element(by=locator[0], value=locator[1])
        element.click()

    def input(self, text, locator):
        input = self.driver.find_element(by=locator[0], value=locator[1])
        input.send_keys(text)

    def press_keycode(self, keycode):
        self.driver.press_keycode(keycode)

    def back(self):
        self.driver.back()
