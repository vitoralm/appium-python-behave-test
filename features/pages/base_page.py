from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

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

    def scroll_down(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(520, 1745)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(539, 994)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
