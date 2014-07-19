import unittest

from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util

from kenix.core.users.services import UserService
from kenix.core.users.models import UserModel


class TestUserService(unittest.TestCase):
    __probability__ = 1
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=self.__probability__)
        self.testbed.init_datastore_v3_stub(consistency_policy=self.policy)
        self.testbed.init_memcache_stub()
        self.testbed.init_blobstore_stub()
        self.testbed.init_files_stub()
        self.testbed.init_urlfetch_stub()
        self.testbed.init_images_stub()
        self.testbed.init_user_stub()
        self.testbed.init_app_identity_stub()
        self.testbed.init_taskqueue_stub(root_path='.')

        self.user = UserModel(full_name='Kenji Noguchi', nickname='Kenji', password='kenji123')
        self.service = UserService()

    def tearDown(self):
        self.testbed.deactivate()

    def test_create(self):
        print self.user.to_dict()
        self.service.create(self.user)
