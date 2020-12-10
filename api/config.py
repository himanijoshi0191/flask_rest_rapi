import os
# cofigration database
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
CORS_HEADERS = 'Content-Type'
