from compare import *
from utils.apiLib import *

@given(u'I connect to the tasks service')
def step_impl(context):
    # result = perform_request('GET', "tasks")
    # print(result.json())
    # data = {'content': 'Test123',
    #        'due_string': 'tomorrow at 12:00',
    #        'due_lang': 'en',
    #        'priority': 4}
    # print(data)
    # result = perform_request('UPDATE',"tasks", 2407910556, data)
     result = perform_request('DELETE', "tasks", 2407910556)
    # if result != None:
     print(result.json())

@given(u'I use "{endpoint}" endpoint')
def step_impl(context, endpoint):
    context.endpoint = endpoint
    context.id = None
    context.data = None
    context.method = None

@given(u'I perform "{method}" method')
def step_impl(context, method):
    context.method = method

@when(u'I send the request')
def step_impl(context):
    context.result = perform_request(context.method, context.endpoint, context.id, context.data)

@then(u'I get status code "{code}"')
def step_impl(context, code):
    #print(context.result.json())
    expect(str(context.result)).to_equal(code)
    print(context.result.code)

@given(u'I sent the proper id: "{id}"')
def step_impl(context, id):
    context.id

@given(u'I will send the following data: "{data}"')
def step_impl(context):
    #json.loads(data)
    context.data = json.loads(context.text)