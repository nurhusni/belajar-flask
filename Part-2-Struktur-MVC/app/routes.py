from app import api, web
from app.controllers import MyController, MyViewController

api.add_resource(MyController.MyController, '/')
web.add_resource(MyViewController.MyViewController, '/')
web.add_resource(MyViewController.MySecondViewController, '/say-my-name')

# Latihan
api.add_resource(MyController.MyFirstController, '/dua-parameter');
api.add_resource(MyController.MySecondController, '/operasi-aritmatika');