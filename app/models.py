from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager
from flask import jsonify
from config import appData

def str_format(strtfm):
    '''
    '''
    return str(strtfm).strip().title()

class Writers(db.Model):
    '''
    '''
    __tablename__ = 'Writers'
    id = db.Column(db.Integer, db.primary_key = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(120), nullable = False, unique = True)
    _password = db.Column(db.String(120), nullable = False)

    def __init__(self, fn, ln, em, _passw = appData['DEFAULT_WRITER_PASS']):
        '''
        '''
        self.first_name = str_format(fn)
        self.last_name = str_format(ln)
        self.email = str_format(em)
        self._password = self.hash_password(_passw)

    @property
    def password():
        '''
        '''
        raise AttributeError('You cannot read the password attribute!')

    @password.setter
    def hash_password(self, passw):
        '''
        '''
        self._password = generate_password_hash(passw)