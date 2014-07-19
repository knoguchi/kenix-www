import unittest
from fabric.api import env, local, task

@task
def run():
    local('dev_appserver.py .')
@task
def test():
    local('nosetests tests')
