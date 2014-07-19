from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel
from kenix.core.users.models import UserModel


class CartModel(EndpointsModel):
    user = ndb.KeyProperty(UserModel)
    line_items = ndb.KeyProperty('LineItemModel', repeated=True)


class LineItemModel(EndpointsModel):
    item = ndb.StringProperty()
    qty = ndb.IntegerProperty()
    uon = ndb.StringProperty()
