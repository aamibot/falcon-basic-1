from werkzeug.security import safe_str_cmp
from api.model.user import User

users = [User(1, "ameer", "asdf")]

username_mapping = {user.username: user for user in users}


def authenticate_user(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user.username
