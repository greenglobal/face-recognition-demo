''' *** '''
# start app

from app import app

PORT = app.config['PORT']
DEBUG = app.config['DEBUG']

app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
