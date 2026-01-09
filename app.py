from backend import create_app, db
from backend.controllers.auth import auth_bp
from backend.controllers.profiles import profiles_bp

app = create_app()
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profiles_bp, url_prefix='/profiles')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()