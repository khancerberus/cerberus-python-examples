from app import db


users_permissions = db.Table(
    "users_permissions",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("permission_id", db.Integer, db.ForeignKey("permissions.id")),
)
