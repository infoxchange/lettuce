import os
from urllib import urlopen
from django.conf import settings
from django.http import HttpResponse
from lettuce import step
from lettuce.django import django_url
from nose.tools import assert_equals

@step(r'django has debug enabled')
def debug_enabled(step):
    assert settings.DEBUG is True

@step(r'django has debug disabled')
def debug_disabled(step):
    assert settings.DEBUG is False

@step(u'Given I start the tests')
def given_i_start_the_tests(step):
    pass

@step(u'the environment variable "(.*)" is \'(.*)\'')
def then_i_see_the_environment_variable_group1_is_group1(step, group1, group2):
    assert_equals(os.environ[group1], group2)

@step(u'I change the view code')
def change_view(step):
    from leaves import views
    def replacement(request):
        return HttpResponse('Changed')
    views.index = replacement

@step(u'The root page says "(.*)"')
def root_page_text(step, text):
    response = urlopen(django_url('/')).read()
    assert_equals(response, text)
