from flask import Flask
from flask_pymongo import PyMongo


application = Flask(__name__)
mongo = PyMongo(application, uri='mongodb://localhost:27017/herberryDB')


import herberry.routes
import herberry.commands
