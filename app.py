from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    #return jsonify(data='Hello techstars!')
    return jsonify('Hello '+name)

if __name__ == "__main__":
    app.run()