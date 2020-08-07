from typing import Optional, List

from main.models.user_model import User


class UserSignUpSchema:
    def __init__(self, json=None):
        if json is not None:
            self.from_dict(json)
        else:
            self.username: Optional[str] = None
            self.email: Optional[str] = None
            self.password: Optional[str] = None

    def from_dict(self, json: dict):
        self.username: Optional[str] = json.get("username", None)
        self.email: Optional[str] = json.get("email", None)
        self.password: Optional[str] = json.get("password", None)
        return self

    def to_dict(self) -> dict:
        dict_form = self.__dict__
        return {k: v for k, v in dict_form.items() if v is not None}


class UserLoginSchema:
    def __init__(self, json=None):
        if json is not None:
            self.from_dict(json)
        else:
            self.email: Optional[str] = None
            self.password: Optional[str] = None

    def from_dict(self, json: dict):
        self.email: Optional[str] = json.get("email", None)
        self.password: Optional[str] = json.get("password", None)
        return self

    def to_dict(self) -> dict:
        dict_form = self.__dict__
        return {k: v for k, v in dict_form.items() if v is not None}


class UserPasswordResetSchema:
    def __init__(self, json=None):
        self.email: Optional[str] = None
        if json is not None:
            self.from_dict(json)

    def from_dict(self, json: dict):
        self.email: Optional[str] = json.get("email", None)
        return self

    def to_dict(self) -> dict:
        dict_form = self.__dict__
        return {k: v for k, v in dict_form.items() if v is not None}


class UserInfoSchema:
    def __init__(self, uid: str = None, username: str = None, email: str = None, user_roles: List[str] = None,
                 json: dict = None):
        if json is not None:
            self.from_dict(json)
        else:
            self.uid: Optional[str] = uid
            self.username: Optional[str] = username
            self.email: Optional[str] = email
            self.user_roles: Optional[List[str]] = user_roles

    def from_dict(self, json: dict):
        self.uid: Optional[str] = json.get("uid", None)
        self.username: Optional[str] = json.get("username", None)
        self.user_roles: Optional[List[str]] = json.get("user_roles", None)
        self.email: Optional[str] = json.get("email", None)
        return self

    def to_dict(self) -> dict:
        dict_form = self.__dict__
        return {k: v for k, v in dict_form.items() if v is not None}

    @staticmethod
    def from_user(user: User):
        user_info_layout = UserInfoSchema()
        user_info_layout.uid = user.firebase_uid
        user_info_layout.username = user.username
        user_info_layout.user_roles = user.user_roles_list
        return user_info_layout
