from bottle import route, run, SimpleTemplate
import face_recognition

template = SimpleTemplate('Hello {{name}}, how are you?')

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template.render(name=name)

run(host='0.0.0.0', port=8085, debug=True)
