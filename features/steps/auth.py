from behave import *

@given(u'flask running')
def flask_is_running(context):
	assert context.client