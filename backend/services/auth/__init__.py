from backend.models.auth import User
from werkzeug.security import generate_password_hash

def create_new_user(email: str, password: str) -> User:
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(email=email, password=hashed_password)
    return new_user