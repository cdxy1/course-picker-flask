from flask import Blueprint, render_template

error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def page_not_found(e):
    return render_template("main/error.html", error=e), 404


@error.app_errorhandler(500)
def internal_server_error(e):
    return render_template("main/error.html", error=e), 500


@error.app_errorhandler(403)
def forbidden(e):
    return render_template("main/error.html", error=e), 403


@error.app_errorhandler(401)
def unauthorized(e):
    return render_template("main/error.html", error=e), 401


@error.app_errorhandler(405)
def method_not_allowed(e):
    return render_template("main/error.html", error=e), 405
