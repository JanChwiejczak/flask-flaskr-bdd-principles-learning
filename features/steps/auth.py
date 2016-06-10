from behave import *


@given(u'we have flask running')
def flask_is_running(context):
    assert context.client


@given(u'we log in with "{username}" and "{password}"')
@when(u'we log in with "{username}" and "{password}"')
def login(context, username, password):
    context.page = context.client.post('/login',
                                       data=dict(username=username, password=password),
                                       follow_redirects=True)
    assert context.page


@when(u'we logout')
def logout(context):
    context.page = context.client.get('/logout', follow_redirects=True)
    assert context.page


@then(u'we should see the alert "{message}"')
def message(context, message):
    assert bytes(message, 'utf-8') in context.page.data
