from behave import *


@given(u'we have flask running')
def flask_is_running(context):
    assert context.client
