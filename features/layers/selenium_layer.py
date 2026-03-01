from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .behave_layer import BehaveLayer


class SeleniumLayer(BehaveLayer):
    def before_all(self, context):
        options = Options()
        options.add_argument('--headless=new')
        context.driver = webdriver.Chrome(options)

    def after_scenario(self, context, scenario):
        if not context.driver.current_url.startswith('data:'):
            context.driver.execute_script(f"window.sessionStorage.clear();")

    def after_all(self, context):
        context.driver.quit()
