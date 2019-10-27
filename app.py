from pymongo import MongoClient
from flask import Flask


application = Flask(__name__)
mongo = MongoClient('mongodb://localhost:27017/herberryDB')


import herberry.routes
import herberry.commands
