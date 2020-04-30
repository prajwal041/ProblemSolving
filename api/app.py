from flask import Flask, request
from flask_restful import Resource, Api
#
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

todo = {}
class Simple(Resource):
    def get(self, todo_id):
        return {todo_id: todo[todo_id]}
    def put(self, todo_id):
        todo[todo_id] = request.form['data']
        return {todo_id: todo[todo_id]}

api.add_resource(HelloWorld, '/app')
api.add_resource(Simple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
