from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z_beep_beep_boop_boop'

import subprocess



@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():	
    # Execute fortune command
    print(str(os.system("fortune")))
    #return '<pre>' + str(os.system("fortune"))+ '</pre>'
    process = subprocess.run(['fortune'],stdout=subprocess.PIPE,universal_newlines=True)
    print(str(process))
    return '<pre>' +process.stdout+ '</pre>'

@app.route('/cowsay/<message>/')
def cowsay(message):
	# Pass message to cowsay command
	return 'Cowsay'

@app.route('/cowfortune/')
def cowfortune():
	return 'cowfortune'
