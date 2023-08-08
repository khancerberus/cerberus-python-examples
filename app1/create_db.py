from run import app
from app import db

from app.models import User, Permission  # noqa


with app.app_context():
    try:
        db.create_all()
        print('Database created!')
    except Exception as e:
        print(e)
        print('Database creation failed!')
