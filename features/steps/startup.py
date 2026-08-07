import requests
from busypie import SECOND

from features.util import wait_at_most


@then(u'the application is available')
@wait_at_most(10, SECOND)
def step_impl(context):
    requests.get("http://localhost:8000")
