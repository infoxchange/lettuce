"""
Step definitions for use with Django.
"""

from lettuce import step
from django.core.management import call_command


@step(r'Fixtures from "([^"]+)" are loaded')
def fixtures_loaded(step, fixtures):
    call_command('loaddata', fixtures, interactive=False)
