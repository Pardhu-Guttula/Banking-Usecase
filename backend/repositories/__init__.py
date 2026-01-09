from backend.models import User, Profile
from backend import db

def get_user_by_email(email: str) -> User:
    return User.query.filter_by(email=email).first()

def create_user(email: str, password: str) -> User:
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def create_profile(user_id: int, first_name: str, last_name: str, date_of_birth: str) -> Profile:
    profile = Profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth
    )
    db.session.add(profile)
    db.session.commit()
    return profile