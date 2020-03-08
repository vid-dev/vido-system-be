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

class Writers(db.Model, UserMixin):
    '''
    '''
    __tablename__ = 'writers'
    id = db.Column( db.Integer, primary_key = True )
    first_name = db.Column( db.String(50), nullable = False )
    last_name = db.Column( db.String(50), nullable = False )
    email = db.Column( db.String(120), nullable = False, unique = True )
    _password = db.Column( db.String(120), nullable = False )

    def __init__( self, fn, ln, em, passw ):
        '''
        '''
        self.first_name = str_format( fn )
        self.last_name = str_format( ln )
        self.email = str_format( em )
        self._password = self.hash_password( passw )

    @property
    def password(self):
        '''
        '''
        raise AttributeError('You cannot read the password attribute!')

    @password.setter
    def hash_password(self, passw):
        '''
        '''
        self._password = generate_password_hash(passw)