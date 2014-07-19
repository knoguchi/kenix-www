from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class UserEmailModel(EndpointsModel):
    email_addr = ndb.StringProperty()


class UserModel(EndpointsModel):
    """
    User model class.
    """
    nickname = ndb.StringProperty()
    full_name = ndb.StringProperty()
    primary_email = ndb.KeyModel('UserEmailModel')
    password = ndb.StringProperty()
    roles = ndb.KeyProperty('RoleModel', repeated=True)


class RoleModel(EndpointsModel):
    """
    Role model class.
    A user must belong to one or more roles
    """
    code = ndb.StringProperty()
    description = ndb.StringProperty()
    permissions = ndb.KeyProperty('PermissionModel', repeated=True)


class PermissionModel(EndpointsModel):
    """
    Permission model class.
    Permission is given to a role.
    """
    code = ndb.StringProperty()
    description = ndb.StringProperty()
