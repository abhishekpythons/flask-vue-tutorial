from flask import Flask, jsonify, request, flash, render_template
from .exts import db
from flask_login import LoginManager
from flask_cors import CORS
from .models import User, Role
from .controllers import controller as controller_blueprint
from werkzeug.security import generate_password_hash


def register_extensions(app):
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'thisisasecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    CORS(app, resources={r"/*": {'origins': "*"}})

    register_extensions(app)
    app.register_blueprint(controller_blueprint)

    @app.errorhandler(404)
    def resource_not_found(e):
        flash(str(e), 'danger')
        return render_template('sitemap.html')

    login_manager = LoginManager()
    login_manager.login_view = 'controller.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
        db.session.commit()
        db.configure_mappers()
        db.session.commit()

        # MAKING ADMIN USER ON LOGIN
        # creating admin AV8 here

        print('trying to create Admin user')
        if not User.query.filter(User.username == 'iAV8').first():
            print('Admin created')
            user = User(username='iAV8',
                        email='AbhishekVerma8.0@gmail.com',
                        password=generate_password_hash('AbhishekVerma'))
            user.roles.append(Role(name='Admin'))
            user.roles.append(Role(name='Creator'))
            db.session.add(user)
            db.session.commit()

    return app
