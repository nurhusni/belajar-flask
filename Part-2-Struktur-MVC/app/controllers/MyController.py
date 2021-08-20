from flask_restful import Resource
from flask import render_template, make_response, request

class MyController(Resource):
    def get(self):
        return {'message': 'Hello World!'}

# Latihan

class MyFirstController(Resource):
    def get(self):
        param_x = request.args.get('x')
        param_y = request.args.get('y')

        if not param_x or not param_y:
            view = render_template('parameter-false.html')
            return make_response(view)
        
        view = render_template('parameter-terisi.html', param_x=param_x, param_y=param_y)
        return make_response(view)

class MySecondController(Resource):
    def get(self):
        method = request.args.get('method')
        first = request.args.get('first')
        second = request.args.get('second')

        if not method or not first or not second:
            view = render_template('parameter-false.html')
            return make_response(view)
        
        int_first = int(first)
        int_second = int(second)

        if (method == "sum"):
            hasil = int_first + int_second
        elif (method == "divide"):
            hasil = int_first / int_second
        elif (method == "sub"):
            hasil = int_first - int_second
        elif (method == "multiply"):
            hasil = int_first * int_second
        else:
            view = render_template('parameter-false.html')
            return make_response(view)

        view = render_template('aritmatika.html', hasil=hasil)
        return make_response(view)
