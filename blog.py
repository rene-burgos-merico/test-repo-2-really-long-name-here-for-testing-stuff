# blog.py - controller

# imports
from flask import Flask, render_templates, request, session,\
    flash, redirect, url_for, g
import sqlite3

# configuration
DATABASE = 'blog.db'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

@route('/')
class Home:
    return 'homepage goes here'
    

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__=='__main__':
    app.run(debug=True)
