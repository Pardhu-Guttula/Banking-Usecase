from flask import request, jsonify
from backend.controllers.profiles import profiles_bp
from backend.models import Profile
from backend import db

@profiles_bp.route('/create', methods=['POST'])
def create_profile():
    data = request.get_json()
    new_profile = Profile(
        user_id=data['user_id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        date_of_birth=data['date_of_birth']
    )
    db.session.add(new_profile)
    db.session.commit()
    return jsonify({'message': 'Profile created successfully'}), 201