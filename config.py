''' *** '''
# config

from os import environ

ENV = environ['APP_ENV']
PORT = int(environ['APP_PORT'])

DEBUG = ENV != 'production'

UPLOAD_FOLDER = '/home/storage/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
