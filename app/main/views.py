from flask import ( 
    url_for, jsonify, render_template, make_response 
)
from . import main

@main.route('/')
def home():
    '''
    '''
    return '<h1> i am the boss </h1>'