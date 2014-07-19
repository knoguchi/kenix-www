import endpoints
from kenix.core import services as core_services
from kenix.cart import services as cart_services
all_services = core_services + cart_services
application = endpoints.api_server(all_services, restricted=False)
