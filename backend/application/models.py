from .exts import db
from flask_login import UserMixin
import uuid


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(1000))
    password = db.Column(db.String(100))

    roles = db.relationship('Role',
                            secondary='user_roles',
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)


class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id',
                                                    ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id',
                                                    ondelete='CASCADE'))


class Product(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(100))
    link = db.Column(db.String(500))
    quantity = db.Column(db.Integer())
    bought = db.Column(db.Boolean())

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'link': self.link,
            'quantity': self.quantity,
            'bought': self.bought
        }
