# Import flask and template operators
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

@app.route('/')
def hello_world():
  return render_template('home.html', title='Hello')

@app.route('/object')
@app.route('/object/<id>')
def hello():
  return render_template('object.html', id=id)

@app.errorhandler(404)
def page_not_found(error):
  print(error)
  return render_template('404.html', errorCode=404, message='Page not found'), 404
