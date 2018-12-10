from flask import Flask
from flask_restful import Api
from user import Users

app = Flask(__name__)
app.secret_key = 'anonymous'
api = Api(app)

api.add_resource(Users, '/users')

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
