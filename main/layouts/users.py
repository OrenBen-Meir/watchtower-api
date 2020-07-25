from main.models.user_model import User


class UserSignUpLayout:
    def __init__(self, json=None):
        self.username = None
        self.email = None
        self.password = None
        if json is not None:
            self.from_dict(json)

    def from_dict(self, json: dict):
        self.username = json.get("username", None)
        self.email = json.get("email", None)
        self.password = json.get("password", None)
        return self

    def to_dict(self) -> dict:
        dict_form = {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
        return {k: v for k, v in dict_form.items() if v is not None}


class UserLoginLayout:
    def __init__(self, json=None):
        self.email = None
        self.password = None
        if json is not None:
            self.from_dict(json)

    def from_dict(self, json: dict):
        self.email = json.get("email", None)
        self.password = json.get("password", None)
        return self

    def to_dict(self) -> dict:
        dict_form = {
            "email": self.email,
            "password": self.password
        }
        return {k: v for k, v in dict_form.items() if v is not None}


class UserInfoLayout:
    def __init__(self, json=None):
        self.username = None
        self.email = None
        self.user_roles = None
        if json is not None:
            self.from_dict(json)

    def from_dict(self, json: dict):
        self.username = json.get("username", None)
        self.email = json.get("email", None)
        self.user_roles = json.get("user_roles", None)
        return self

    def to_dict(self) -> dict:
        dict_form = {
            "username": self.username,
            "email": self.email,
            "user_roles": self.user_roles
        }
        return {k: v for k, v in dict_form.items() if v is not None}

    def from_user(self, user: User):
        self.username = user.username
        self.user_roles = user.user_roles
