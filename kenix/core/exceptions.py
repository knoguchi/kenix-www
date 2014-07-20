import httplib
from endpoints.api_exceptions import ServiceException

class KenixException(ServiceException):
    def __init__(self):
        msg = "%s: %s" % (self.kenix_code, self.kenix_message)
        super(KenixException, self).__init__(msg)

class UserEmailIdentityExists(KenixException):
    kenix_code = 10000
    kenix_message = 'the email address provided already exists'
    http_status = httplib.BAD_REQUEST

class UserExists(KenixException):
    kenix_code = 10001
    kenix_message = 'the user already exists'
    http_status = httplib.BAD_REQUEST
