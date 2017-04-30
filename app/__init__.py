''' *** '''
# app init
from os import path
from flask import Flask, request, redirect, jsonify, url_for, render_template, send_from_directory
from flask_assets import Bundle, Environment
from werkzeug.utils import secure_filename

# Define the WSGI application object
app = Flask(__name__, static_url_path='/static')

# Configurations
app.config.from_object('config')

bundles = {
  'common_css': Bundle(
    'css/vendor/spectre.min.css',
    'css/vendor/spectre-icons.min.css',
    'css/custom.css',
    output='gen/common.css'
  ),
  'common_js': Bundle(
    'js/vendor/qwest.min.js',
    'js/vendor/vue.min.js',
    'js/vendor/doc.min.js',
    'js/app.js',
    output='gen/main.js'
  )
}

assets = Environment(app)

assets.register(bundles)

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
  return render_template('home.html', title='Demo')

@app.route('/people')
@app.route('/people/<id>')
def people():
  return render_template('people.html', title='People', id=id)


@app.route('/css/<path:path>')
def static_file(loca):
  return app.send_static_file('css/' + loca)

@app.route('/upload', methods=['POST'])
def upload_file():
  fileToSave = request.files['fileToReco']
  if fileToSave and fileToSave.filename == '':
    return jsonify(
      error=1,
      message='No file to save'
    )
  if allowed_file(fileToSave.filename):
    filename = secure_filename(fileToSave.filename)
    fileToSave.save(path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify(
      error=0,
      name=filename
    )

@app.errorhandler(404)
def page_not_found(error):
  print (error)
  return render_template('404.html', errorCode=404, message='Page not found'), 404
