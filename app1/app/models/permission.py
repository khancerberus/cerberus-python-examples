from app import db

from app.models.rel_users_permissions import users_permissions


class Permission(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    users = db.relationship(
        'User',
        secondary=users_permissions,
        back_populates='permissions'
    )
