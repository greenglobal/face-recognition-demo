from app import app

port = app.config['PORT']
debug = app.config['DEBUG']

app.run(host='0.0.0.0', port=port, debug=debug)
