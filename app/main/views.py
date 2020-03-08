from flask import ( 
    url_for, jsonify, render_template, make_response 
)
from . import main
from flask_login import login_required



@main.route('/')
@login_required
def home():
    '''
    '''
    return '<h1> i am the boss </h1>'