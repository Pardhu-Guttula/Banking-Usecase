from werkzeug.security import generate_password_hash
from backend.repositories import create_user as repo_create_user
from backend.models import User

def register_user(email: str, password: str) -> User:
    hashed_password = generate_password_hash(password, method='sha256')
    return repo_create_user(email, hashed_password)