from protorpc import messages

class AuthRequest(messages.Message):
    email = messages.StringField(1)
    password = messages.StringField(2)


class AuthToken(messages.Message):
    """
    Authentication Token
    """
    auth_token = messages.StringField(1)
    user = messages.StringField(2)
    logout_status = messages.BooleanField(3)

class CreateUserRequest(messages.Message):
    email = messages.StringField(1)
    password = messages.StringField(2)
    lastname = messages.StringField(3)
    firstname = messages.StringField(4)

