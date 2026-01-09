from backend.models.auth import User
from backend import db

def add_user(user: User) -> None:
    db.session.add(user)
    db.session.commit()

def get_user_by_email(email: str) -> User:
    return User.query.filter_by(email=email).first()