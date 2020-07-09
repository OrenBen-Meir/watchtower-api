from main.layouts.users import UserLayout
from main.application import db, bcrypt
from main.business_rules import user_rules
from main.security import roles

def register_user(user_layout: UserLayout):
    user_layout.id = None
    user_layout.user_roles = [roles.regular]
    user_rules.user_creation_rules(user_layout)
    
    user = user_layout.to_user()
    user.password = bcrypt.generate_password_hash(user.password).decode('utf-8')   
    db.session.add(user)
    db.session.commit()

    response_layout = UserLayout().from_user(user)
    response_layout.password = None
    return response_layout