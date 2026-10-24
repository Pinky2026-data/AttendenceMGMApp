
#
from flask import Flask, redirect, url_for,  render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

from config import Config

# Initialize extensions (unbound)
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Import and register blueprints
    from attendance_app.auth import auth_bp
    from attendance_app.admin import admin_bp
    from attendance_app.student import student_bp
    from attendance_app.attendance import attendance_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(attendance_bp)

    # Root route: redirect to login or dashboard
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            if current_user.role == 'admin':
                return redirect(url_for('admin.admin_home'))
            else:
                return redirect(url_for('student.dashboard'))
        return render_template('Home.html')


    # Create database tables
    with app.app_context():
        db.create_all()

    return app
