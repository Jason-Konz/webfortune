from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():	
   # Execute fortune command
    process = subprocess.run(['fortune'],stdout=subprocess.PIPE)
    return '<pre>' +process.stdout.decode()+ '</pre>'

@app.route('/cowsay/<message>/')
def cowsay(message):
   # Pass message to cowsay command
    process = subprocess.run(['cowsay', message],stdout=subprocess.PIPE)
   
    return '<pre>' + process.stdout.decode()+'</pre>'

@app.route('/cowfortune/')
def cowfortune():
    process = subprocess.run(['fortune'],stdout=subprocess.PIPE)
    result = subprocess.run(['cowsay', process.stdout.decode()],stdout=subprocess.PIPE)
    return '<pre>' + result.stdout.decode()+'</pre>'
