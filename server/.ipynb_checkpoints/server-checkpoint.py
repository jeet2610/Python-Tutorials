from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to handle GET requests
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, this is a GET request!'

# Endpoint to handle POST requests
@app.route('/post-example', methods=['POST'])
def post_example():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from POST request
        return jsonify({'received_data': data}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
