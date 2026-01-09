from backend.models.auth import User

def get_user_by_email(email: str) -> User:
    return User.query.filter_by(email=email).first()

def create_user(email: str, password: str) -> User:
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user