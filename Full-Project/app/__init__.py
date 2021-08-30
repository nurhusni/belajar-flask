from flask import Flask

app = Flask(__name__, template_folder="views")
api = Api(app, prefix="/api")
web = Api(web)

from app import routes