import unittest
from fabric.api import env, local, task

@task
def run():
    local('dev_appserver.py .')
@task
def test():
    local('nosetests tests')
@task
def collectdeps():
    local('python manage.py collectdeps -r requirements.txt')
