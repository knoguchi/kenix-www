import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from .messages import Cart, LineItem
from .models import CartModel, LineItemModel
from .api import kenix_cart_api

@kenix_cart_api.api_class(resource_name='carts')
class CartService(remote.Service):
    """
    Cart Service v1
    """

    @CartModel.query_method(query_fields=('limit', 'pageToken'),
                            path='carts', name='index')
    def index(self, query):
        """
        List of carts
        """
        return query

    @CartModel.method(path='carts/{id}', http_method='GET', name='get')
    def get(self, cart):
        """
        Get a cart
        @param cart:
        @return:
        """
        if not cart.from_datastore:
            raise endpoints.NotFoundException('Cart not found')
        return cart

    @CartModel.method(path='carts', name='create')
    def create(self, cart):
        """
        Create a cart
        """
        # do some validation
        cart.put()
        return cart

    @CartModel.method(path='carts/{id}', http_method='PUT', name='update')
    def update(self, cart):
        """
        Update a cart
        @param cart:
        @return cart:
        """
        if not cart.from_datastore:
            raise endpoints.NotFoundException('Cart not found')
        cart.put()
        return cart
