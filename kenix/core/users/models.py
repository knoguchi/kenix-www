import hashlib
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class UserEmailIdentityModel(EndpointsModel):
    email = ndb.StringProperty()


class UserModel(EndpointsModel):
    """
    User model class.
    """
    nickname = ndb.StringProperty(indexed=False)
    firstname = ndb.StringProperty(indexed=False)
    lastname = ndb.StringProperty(indexed=False)
    password = ndb.StringProperty(indexed=False)

    email_identity = ndb.KeyProperty(kind='UserEmailIdentityModel')
    roles = ndb.KeyProperty(kind='RoleModel', repeated=True)

    @classmethod
    def get_by_email(cls, email):
        email_hash = hashlib.sha1(email).hexdigest()
        email_identity_key = ndb.Key('UserEmailIdentityModel', email_hash)
        return cls.query(ancestor=email_identity_key).fetch(1)


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
