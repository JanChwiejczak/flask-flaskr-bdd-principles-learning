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


@when(u'we add a new entry with "{title}" and "{text}" as the title and text')
def successful_post(context, title, text):
    context.page = context.client.post('/add', data=dict(title=title, text=text), follow_redirects=True)
    assert context.page


@step("we are not logged in")
def not_logged_in(context):
    context.page = context.client.get('/logout', follow_redirects=True)


@then('we should see a "{status}" status code')
def step_impl(context, status):
    context.page = context.client.post('/add', data=dict(title='title', text='text'), follow_redirects=True)
    assert context.page._status_code == int(status)


@step('we should see the post with "{title}" and "{text}" in title and text')
def step_impl(context, title, text):
    title = bytes(title, 'utf-8')
    text = bytes(text, 'utf-8')
    context.page = context.client.get('/index', follow_redirects=True)
    assert title and text in context.page.data