from backend.config import create_app, db
from backend.controllers.auth import auth_bp

app = create_app()
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()