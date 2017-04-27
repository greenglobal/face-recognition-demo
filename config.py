from os import environ

ENV = environ['APP_ENV']
PORT = int(environ['APP_PORT'])

DEBUG = ENV != 'production'

