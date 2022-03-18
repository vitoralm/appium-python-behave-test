from appium import webdriver
from app.application import Application


def before_scenario(context, scenario):
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities={'platformName': 'Android',
                                                                                            'platformVersion': '8.0',
                                                                                            'deviceName': 'Android 6.0 x86',
                                                                                            'automationName': 'UiAutomator2',
                                                                                            'app': '/home/vitoralm/workspace/Android-App-Demo/app/build/outputs/apk/debug/app-debug.apk',
                                                                                            'appPackage': 'com.codepath.android.booksearch',
                                                                                            "appWaitActivity": '.activities.BookListActivity',
                                                                                            'newCommandTimeout': 300
                                                                                            })

    context.driver.implicitly_wait(30)
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()
