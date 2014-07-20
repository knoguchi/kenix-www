import logging
import hashlib
import endpoints
from protorpc import remote
from google.appengine.api import users
from google.appengine.ext import ndb
from .models import UserModel, UserEmailIdentityModel
from kenix.core.api import kenix_core_api
from kenix.core.exceptions import UserEmailIdentityExists, UserExists
# kenix.core.users relative
from .messages import AuthRequest, AuthToken, CreateUserRequest
log = logging.getLogger(__name__)




@kenix_core_api.api_class(resource_name='users')
class UserService(remote.Service):
    """
    Users API v1
    """

    @UserModel.query_method(query_fields=('limit', 'pageToken'),
                            path='users', name='index')
    def index(self, query):
        """
        List of users
        """
        return query

    @UserModel.method(path='users/{id}', http_method='GET', name='get')
    def get(self, user):
        """
        Get a user
        @param user:
        @return:
        """
        if not user.from_datastore:
            raise endpoints.NotFoundException('User not found')
        return user

    @ndb.transactional(xg=True)
    @endpoints.method(CreateUserRequest, UserModel.ProtoModel(fields=['id']),
                      path='users', http_method='POST', name='create', )
    def create(self, request):
        """
        Create a user.
        """
        # user input string is validated by Message schema
        email = request.email.lower().strip()
        email_hash = hashlib.sha1(email).hexdigest()

        # Do not allow same ident to be created
        email_identity = UserEmailIdentityModel.get_by_id(email_hash)
        if email_identity:
            raise UserEmailIdentityExists()

        password_hash = hashlib.sha1(request.password).hexdigest()
        user = UserModel.get_by_email(request.email)
        if user:
            raise UserExists()
        # End of validation

        email_identity = UserEmailIdentityModel(
            id=email_hash,
            email=request.email,
            )
        email_identity.put()
        user = UserModel(
            nickname=request.firstname,
            firstname=request.firstname,
            lastname=request.lastname,
            password=password_hash,
            email_identity=email_identity.key
            )
        user.put()
        return user.ToMessage(fields=['id'])

    @UserModel.method(path='users/{id}', http_method='PUT', name='update')
    def update(self, user):
        """
        Update a user
        @param user:
        @return user:
        """

        if not user.from_datastore:
            raise endpoints.NotFoundException('User not found')
        user.put()
        return user

    # @UserModel.method(path='users', http_method='POST',
    # name='_auth')
    # def _auth(self, query):
    #     """
    #     Authenticate user by user id and password, or cookie.
    #     """
    #     log.error(query)
    #     current_user = endpoints.get_current_user()
    #     if not current_user:
    #         raise endpoints.NotFoundException('User not authenticated')
    #     return current_user

    # request_message=message_types.VoidMessage,
    # response_message=message_types.VoidMessage,
    # name=None,
    # path=None,
    # http_method='POST',
    # cache_control=None,
    # scopes=None,
    # audiences=None,
    # allowed_client_ids=None,
    # auth_level=None

    @endpoints.method(AuthRequest, AuthToken,
                      path='users/auth', http_method='POST',
                      name='auth')
    def auth(self, *args, **kw):
        """
        Authenticate a user by email and password
        @param args:
        @param kw:
        @return:
        """
        user = users.get_current_user()
        token = AuthToken()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        #else:
        #    self.redirect(users.create_login_url(self.request.uri))

        log.error(args)
        log.error(kw)
        token.auth_token = 'aaa'
        token.user = 'kenji'
        return token

    @endpoints.method(AuthRequest, AuthToken,
                      path='users/logout', http_method='POST',
                      name='logout')
    def logout(self, *args, **kw):
        """
        Logout a user
        @param self:
        @param args:
        @param kw:
        @return:
        """
        token = AuthToken()
        token.auth_token = ''
        token.user = ''
        token.logout_status = True
        return token

