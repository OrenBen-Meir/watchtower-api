from itsdangerous import TimedJSONWebSignatureSerializer as Serializer              # For email Reset JSON token! 
from flask import current_app
from main.application import db, login_manager                                           # Resolves issue with circular imports! Login manager is a flask-extension
from flask_login import UserMixin 

@login_manager.user_loader 
def laod_user(user_id):
    return User.query.get(int(user_id))  

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(30), unique=True, nullable=False)
    email = db.Column('email', db.String(120), unique=True, nullable=False)
    password = db.Column('password', db.String(60), nullable=False)
    user_roles = db.Column('user_roles', db.String(None), nullable=False)                 

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')                        # s.dumps returns a payload! decode 'utf-8' makes sure were returning a string and not bytes 

    @staticmethod                                                                   # This method needs to be static so that it cannot reference self, only the token can be passed in! 
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None

        return User.query.get(user_id)                                              # So if everything goes smoothly, and no exceptions go off, return the user in the database with user_id.

    @property
    def user_roles_list(self) -> list:
        return self.user_roles.split(", ")

    @user_roles_list.setter
    def user_roles_list(self, roles : list):
        self.user_roles = ", ".join(roles)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"