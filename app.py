from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config
from models import db, bcrypt
from routes import init_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Rate limiter - modern Flask-Limiter ≥3.0 syntax
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=[app.config['RATELIMIT_DEFAULT']]
)

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

# Secure headers
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self' cdn.jsdelivr.net 'unsafe-inline'; style-src 'self' cdn.jsdelivr.net 'unsafe-inline' fonts.googleapis.com"
    return response

# Create all tables if they don't exist
with app.app_context():
    db.create_all()

init_routes(app, limiter)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)