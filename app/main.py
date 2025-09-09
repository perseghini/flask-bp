import os

from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
from .helpers.logger_helper import get_logger
from .helpers.file_helper import dir_last_updated

main = Blueprint("main", __name__)

logger = get_logger()


@main.route("/")
# @login_required
def index():
    dir_checksum = dir_last_updated("app/static")
    return render_template(
        "main.html",
        dir_checksum=dir_checksum,
    )


@main.route("/hash", methods=["GET", "POST"])
def get_hash():
    hash_value = None
    if request.method == "POST":
        hash_value = generate_password_hash(request.form.get("pwd"))
    return render_template(
        "hash.html",
        hash_value=hash_value,
    )
