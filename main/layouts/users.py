from main.application import bcrypt
from main.models.user_model import User


class UserLayout:
    """
    A json convertible class for user related APIs.
    """

    def __init__(self):
        self.id = None
        self.username = None
        self.email = None
        self.password = None
        self.user_roles = None
        self.remember = None  # only for logging in

    def from_dict(self, json: dict):
        self.id = json.get("id", None)
        self.username = json.get("username", None)
        self.email = json.get("email", None)
        self.password = json.get("password", None)
        self.user_roles = json.get("user_roles", None)
        return self

    def to_dict(self) -> dict:
        dict_form = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "user_roles": self.user_roles
        }
        return {k: v for k, v in dict_form.items() if v is not None}

    def from_user(self, user: User, include_password=True):
        self.id = user.id
        self.username = user.username
        self.email = user.email
        if include_password:
            self.password = user.password
        self.user_roles = user.user_roles_list
        return self

    def to_user(self, password_encrypted=False) -> User:
        """
        Converts user layout to user. If password field is not encrypted,
        set the password_encrypted parameter to be true
        """
        user = User(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password
        )
        if password_encrypted:
            user.password = bcrypt.generate_password_hash(user.password).decode('utf-8')
        user.user_roles_list = self.user_roles
        return user
