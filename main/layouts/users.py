from main.models.user_model import User

class UserLayout:
    def __init__(self):
        self.id = None
        self.username = None
        self.email = None
        self.password = None
        self.user_roles = None

    def from_dict(self, json: dict):
        self.id = json.get("id", None)
        self.username = json.get("username", None)
        self.email = json.get("email", None)
        self.password = json.get("password", None)
        self.user_roles = json.get("user_roles", None)
        return self

    def to_dict(self) -> dict:
        return {
            "id" : self.id,
            "username" : self.username,
            "email" : self.email,
            "password" : self.password,
            "user_roles" : self.user_roles
        }
    
    def from_user(self, user: User):
        self.id = user.id
        self.username = user.username
        self.email = user.email
        self.password = user.password
        self.user_roles = user.user_roles_list
        return self
    
    def to_user(self) -> User:
        user = User(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password
        )
        user.user_roles_list = self.user_roles
        return user
    