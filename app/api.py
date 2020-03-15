import hashlib
import random
import string

from flask import request
from flask import current_app as app
from .models import db, User, AuthToken
from datetime import datetime, timedelta

@app.route('/api/users', methods=['POST'])
def create_user():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    if username != None and password != None and email != None:

        response = None
        try:
            new_user = User(
                username=username,
                password=hashlib.sha256(str(password).encode('utf-8')).hexdigest(),
                email=email,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )

            db.session.add(new_user)
            db.session.commit()

            response = response = {
                'status': 'success',
                'token': 'User regisrtered successfully.'
            }
        except Exception as error:
            response = response = {
                'status': 'failed',
                'token': 'User registration failed.'
            }

    return response

@app.route('/api/login', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')

    response = None
    try:
        authenticated = User.query.filter(
            User.username == username,
            User.password == hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        ).first()

        if authenticated != None:

            token = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(64)])
            if len(authenticated.auth_tokens) > 0:
                token = authenticated.auth_tokens[0].token if authenticated.auth_tokens[0].expires_at <= datetime.now() \
                    else authenticated.auth_tokens[0].token
            else:

                auth_token = AuthToken(
                    user_id=authenticated.id,
                    token=token,
                    expires_at= datetime.now() + timedelta(seconds=app.config.get('SESSION_LENGTH')),
                    created_at=datetime.now()
                )
            
                db.session.add(auth_token)
                db.session.commit()

            response = {
                'status': 'success',
                'token': token
            }
        else:
            response = {
                'status': 'failed',
                'message': 'Login failed'
            }
    except Exception as error:
        response = {
            'status': 'failed',
            'message': 'An error occured: {}'.format(error)
        }

    return response
