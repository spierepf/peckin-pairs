import os

import dotenv
from busypie import SECOND
from selenium.webdriver.common.by import By

from features.util import wait_at_most


@when(u'a user logs in as the superuser')
@wait_at_most(2, SECOND)
def step_impl(context):
    dotenv.load_dotenv(dotenv.find_dotenv())
    context.driver.get(f"http://localhost:8000/admin")
    context.driver.find_element(By.ID, "id_username").send_keys(os.getenv('DJANGO_SUPERUSER_USERNAME'))
    context.driver.find_element(By.ID, "id_password").send_keys(os.getenv('DJANGO_SUPERUSER_PASSWORD'))
    context.driver.find_element(By.XPATH, '//div[@class="submit-row"]/input').click()


@then(u'the user will see the admin page')
@wait_at_most(2, SECOND)
def step_impl(context):
    assert context.driver.find_element(By.ID, "user-tools") is not None
