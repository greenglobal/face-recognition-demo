from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

all_css = Bundle('css/style.css', less,
                 filters='cssmin', output="gen/all.css")
assets.register('all_css', all_css)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/people')
@app.route('/people/<name>')
def hello(name=None):
  return render_template('people.html', name=name)

@app.errorhandler(404)
def page_not_found(error):
  print(error)
  return render_template('404.html', errorCode=404, message='Page not found'), 404
