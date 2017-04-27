# Import flask and template operators
from flask import Flask, url_for, render_template
from flask_assets import Bundle, Environment

# Define the WSGI application object
app = Flask(__name__, static_url_path='/static')

# Configurations
app.config.from_object('config')

bundles = {
  'common_css': Bundle(
    'css/vendor/spectre.min.css',
    'css/custom.css',
    output='gen/common.css'
  )
}

assets = Environment(app)

assets.register(bundles)

@app.route('/')
def home():
  return render_template('home.html', title='Hello')

@app.route('/object')
@app.route('/object/<id>')
def object():
  return render_template('object.html', id=id)

@app.route('/css/<path:path>')
def static_file(path):
    return app.send_static_file('css/' + path)

@app.errorhandler(404)
def page_not_found(error):
  print(error)
  return render_template('404.html', errorCode=404, message='Page not found'), 404
