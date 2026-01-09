from backend.repositories import create_profile as repo_create_profile
from backend.models import Profile

def create_profile(user_id: int, first_name: str, last_name: str, date_of_birth: str) -> Profile:
    return repo_create_profile(user_id, first_name, last_name, date_of_birth)