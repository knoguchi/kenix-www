import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'carts'


class Product(messages.Message):
    """
    Product message
    """
    sku = messages.StringField(100)


class LineItem(messages.Message):
    """
    Line item
    """
    item = messages.MessageField(Product, 1)
    qty = messages.IntegerField(2)
    uom = messages.StringField(10)


class Cart(messages.Message):
    """
    Collection of LineItems
    """
    line_items = messages.MessageField(LineItem, 1, repeated=True)