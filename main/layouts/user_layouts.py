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
    def __init__(self, username=None, email=None, user_roles=None, json=None):
        if json is not None:
            self.from_dict(json)
        else:
            self.username = username
            self.email = email
            self.user_roles = user_roles

    def from_dict(self, json: dict):
        self.username = json.get("username", None)
        self.user_roles = json.get("user_roles", None)
        self.email = json.get("email", None)
        return self

    def to_dict(self) -> dict:
        dict_form = {
            "username": self.username,
            "email": self.email,
            "user_roles": self.user_roles
        }
        return {k: v for k, v in dict_form.items() if v is not None}

    @staticmethod
    def from_user(user: User):
        user_info_layout = UserInfoLayout()
        user_info_layout.username = user.username
        user_info_layout.user_roles = user.user_roles_list
        return user_info_layout
