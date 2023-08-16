from cerberus import Validator

from app import db
from app.models.rel_users_permissions import users_permissions


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    permissions = db.relationship(
        "Permission", secondary=users_permissions, back_populates="users"
    )

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def json(self):
        return {"id": self.id, "name": self.name, "age": self.age}


def check_name_length(field, value, error):
    if len(value) < 3:
        error(field, "name must be at least 3 characters long")

    if len(value) > 100:
        error(field, "name must be less than 100 characters long")


user_schema = {
    "name": {"type": "string", "required": True, "check_with": check_name_length},
    "age": {"type": "integer", "required": True, "min": 0, "max": 150},
}

# Used for validating the entire user creation
def validate_user(user_data, update=False):
    validator = Validator()
    validator.allow_unknown = True # type: ignore
    validator.validate(user_data, user_schema, update=update) # type: ignore
    return validator
