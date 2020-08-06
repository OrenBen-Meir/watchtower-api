from main.models.user_model import User


class UserSignUpSchema:
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


class UserLoginSchema:
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


class UserInfoSchema:
    def __init__(self, uid=None, username=None, email=None, user_roles=None, json=None):
        if json is not None:
            self.from_dict(json)
        else:
            self.uid = uid
            self.username = username
            self.email = email
            self.user_roles = user_roles

    def from_dict(self, json: dict):
        self.uid = json.get("uid", None)
        self.username = json.get("username", None)
        self.user_roles = json.get("user_roles", None)
        self.email = json.get("email", None)
        return self

    def to_dict(self) -> dict:
        dict_form = {
            "uid": self.uid,
            "username": self.username,
            "email": self.email,
            "user_roles": self.user_roles
        }
        return {k: v for k, v in dict_form.items() if v is not None}

    @staticmethod
    def from_user(user: User):
        user_info_layout = UserInfoSchema()
        user_info_layout.uid = user.firebase_uid
        user_info_layout.username = user.username
        user_info_layout.user_roles = user.user_roles_list
        return user_info_layout
