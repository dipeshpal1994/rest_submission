from logging import error
from types import MethodType
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/<string:name>', methods=['GET'])
def hello_world(name: str):
    return jsonify(data=name), 200
    #Put in browser <http://127.0.0.1:5000/Dipu>

 
 
if __name__ == "__main___":
    app.run()


'''
# With JSON
from logging import error
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get("name")
    return jsonify(data=name), 200
    #return jsonify(error='Something bad happened.'), 404
    #return jsonify(data='Hi Dipesh... Welcome to the world of Flask.')

 
 
if __name__ == "__main___":
    app.run()


# Without JSON
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi Dipesh... Welcome to the world of Flask.'
    
 
 
if __name__ == "__main___":
    app.run()
'''