#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.auth.auth import Auth
from api.v1.views import app_views
from api.v1.auth.session_auth import SessionAuth
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
# get AUTH_TYPE environment variable
AUTH_TYPE = os.getenv('AUTH_TYPE')

if AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE == 'session_auth':
    auth = SessionAuth()
else:
    auth = Auth()


@app.before_request
def before_request():
    """Flask method before request"""
    if auth is None:
        # if no auth is provided do nothing
        return

    # list of paths that doesn;t require authentication
    excluded_paths = [
        '/api/v1/status/',
        'api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login/'
    ]

    # use require_auth to check if path requires authentication
    if not auth.require_auth(request.path, excluded_paths):
        # if path doesn't, do nothing
        return

    # IF AUTHORIZATION HEADER IS MISSING and session cookie, RAISE 401 ERROR
    if (auth.authorization_header(request) is None and
            auth.session_cookie(request) is None):
        abort(401)

    # assign authenticated user to request.current_user
    request.current_user = auth.current_user(request)

    # IF CURRENT USER NOT FOUND, RAISE 403 ERROR
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Unauthorized handler
    Args:
        error

    Returns:
        _type_: jsonify
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    forbidden error handler
    Args:
        error (_type_): code 403

    Returns:
        str: jsonify
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
