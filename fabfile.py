import unittest
from fabric.api import env, local, task

@task
def test():
    local('nosetests tests')
