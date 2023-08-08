from flask import Blueprint


app_bp = Blueprint('app', __name__)

from . import admin_user  # noqa
