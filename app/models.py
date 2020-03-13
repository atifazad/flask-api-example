from . import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(30),
        index=False,
        unique=False,
        nullable=False
    )

    email = db.Column(
        db.String(80),
        index=False,
        unique=True,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        index=False,
        unique=True,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        index=False,
        unique=True,
        nullable=False
    )

    def __repr(self):
        return '<User {}>'.format(self.username)
