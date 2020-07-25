from flask_sqlalchemy import Pagination

from main.application import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True)
    firebase_uid = db.Column('firebase_uid', db.String(128), nullable=False)
    username = db.Column('username', db.String(30), unique=True, nullable=False)
    user_roles = db.Column('user_roles', db.String(None), nullable=False)

    @property
    def user_roles_list(self) -> list:
        return self.user_roles.split(",")

    @user_roles_list.setter
    def user_roles_list(self, roles: list):
        self.user_roles = ",".join(roles)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class UserQuery(object):
    @staticmethod
    def get_users_by_pagination(page: int, per_page: int) -> Pagination:
        return User.query.order_by(User.id.asc()).paginate(page, per_page, error_out=False)
