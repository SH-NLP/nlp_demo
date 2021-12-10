# config.py
 
import os
BASE_DIR = os.path.dirname(__file__)
 
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'nlp_demo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
TEMPLATES_AUTO_RELOAD = True
