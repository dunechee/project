import urllib
from urllib.parse import urljoin
from behave import given, when, then

@given(u'we submit a product')
def user_on_product_newpage(context):
	base_url = urllib.request.url2pathname(context.test_case.live_server_url)
	print(base_url)
	open_url = urljoin(base_url,'/create/')
	context.browser.get(open_url)


@when(u'we fill in the form')
def user_fills_in_the_form(context):
	# use print(context.browser.page_source) to aid debugging
	# only prints page source if there is an error in the step
	print(context.browser.page_source)
	name_textfield = context.browser.find_element('name', 'name')
	name_textfield.send_keys('thing one')
	price_textfield = context.browser.find_element('name','price')
	price_textfield.send_keys(3)
	context.browser.find_element('name','submit').click()


@then(u'it succeeds')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it succeeds')