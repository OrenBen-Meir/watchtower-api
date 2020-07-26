from flask_sqlalchemy import Pagination
from sqlalchemy import and_, true, desc

from main.application import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True)
    firebase_uid = db.Column('firebase_uid', db.String(128), nullable=False)
    username = db.Column('username', db.String(30), unique=False, nullable=False)
    user_roles = db.Column('user_roles', db.String(None), nullable=False)
    active = db.Column('active', db.Boolean, nullable=False, default=True)

    @property
    def user_roles_list(self) -> list:
        return self.user_roles.split(",")

    @user_roles_list.setter
    def user_roles_list(self, roles: list):
        self.user_roles = ",".join(roles)

    def __repr__(self):
        return str({
            "id": self.id,
            "firebase_uid": self.firebase_uid,
            "username": self.username,
            "user_roles": self.user_roles,
            "active": self.active
        })


class UserQuery(object):
    @staticmethod
    def get_first_active_user_with_firebase_uid(firebase_uid: str) -> User:
        return User.query.filter(and_(User.firebase_uid == firebase_uid, User.active == true())).order_by(desc(User.id)).first()

    @staticmethod
    def active_users_with_firebase_uid(firebase_uid: str):
        return User.query.filter(and_(User.firebase_uid == firebase_uid, User.active == true()))

    @staticmethod
    def exists_active_user_with_firebase_uid(firebase_uid: str) -> bool:
        return User.query.filter(and_(User.firebase_uid == firebase_uid, User.active == true())).count() > 0

    @staticmethod
    def exists_active_user_with_username(username: str):
        return User.query.filter(and_(User.username == username, User.active == true())).count() > 0

    @staticmethod
    def get_active_users_by_pagination(page: int, per_page: int) -> Pagination:
        return User.query.order_by(User.id.asc()).filter(User.active == true()).paginate(page, per_page, error_out=False)
