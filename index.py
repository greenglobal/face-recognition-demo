from os import environ
from bottle import route, run, SimpleTemplate
import face_recognition as fare
from trainer import Trainer

ENV = environ['APP_ENV']
PORT = environ['APP_PORT']

template = SimpleTemplate('Hello {{name}}, how are you?')

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template.render(name = name)


Trainer.train()

run(host='0.0.0.0', port = PORT, debug = ENV == 'production')
