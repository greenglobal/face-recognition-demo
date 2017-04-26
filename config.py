from os import environ


class config:
  def __init__(self):
    self.ENV = environ['APP_ENV']
    self.PORT = environ['APP_PORT']

