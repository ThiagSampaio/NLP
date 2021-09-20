import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False

def teste(uri = SQLALCHEMY_DATABASE_URI, key = SECRET_KEY):
    print(f'Esta é a sql: {uri}')
    print(key)