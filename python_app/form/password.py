import json

import dotenv
import requests
from flask import (
    Blueprint, redirect, render_template, request
)

bp = Blueprint('password', __name__)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    error = None
    if check_password_exist():
        return redirect("/")
    if request.method == 'POST':
        password = request.form['password']

        if not password:
            error = 'Password is required.'

        if error is None:
            dotenv_file = dotenv.find_dotenv("../.env")
            dotenv.load_dotenv(dotenv_file)
            dotenv.set_key(dotenv_file, "PASSWORD", password)
            return redirect("/")

    return render_template('password/register.html', error=error)


@bp.route('/', methods=('GET', 'POST'))
def root_page():
    if check_password_exist():
        public_ip = json.loads(requests.get("https://ipinfo.io/json").content)["ip"]
        message = "Welcome ! You can access R-studio here:"
        url = f"http://{public_ip}:8787"
        return render_template('base.html', message=message, url=url)
    else:
        return redirect("/register")


def check_password_exist():
    config = dotenv.dotenv_values("../.env")
    if config["PASSWORD"]:
        return True
    return False
