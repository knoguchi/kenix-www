import os
from fabric.api import env, local, task

PROJECT_ROOT=os.path.abspath(os.path.dirname(__file__))
@task
def run():
    local('dev_appserver.py .')
@task
def test():
    local('nosetests tests')
@task
def collectdeps():
    ONE_LEVEL_ABOVE = os.path.abspath(os.path.join(PROJECT_ROOT, '..'))
    local('cd %s && rm -rf endpoints-proto-datastore && git clone https://github.com/GoogleCloudPlatform/endpoints-proto-datastore' % ONE_LEVEL_ABOVE)
    local('mkdir -p %s/libs' % PROJECT_ROOT)
    local('cd %s/libs && rm endpoints_proto_datastore && ln -s ../../endpoints-proto-datastore/endpoints_proto_datastore' % PROJECT_ROOT)
    local('python manage.py collectdeps -r requirements.txt')
