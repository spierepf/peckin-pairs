import requests
from busypie import SECOND

from features.util import wait_at_most


@then(u'the application is available')
@wait_at_most(1, SECOND)
def step_impl(context):
    assert 200 == requests.get("http://localhost:8000").status_code
