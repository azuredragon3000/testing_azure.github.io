import socket
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS support for all routes

def find_free_port():
    """Find a free port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))  # Bind to localhost and let the OS assign a free port
    _, port = sock.getsockname()  # Get the assigned port
    sock.close()  # Close the socket
    return port

@app.route('/')
def home():
    return 'Hello from Flask!'

@app.route('/my-first-api', methods=['GET'])
def hello():
    name = request.args.get('name')
    if not name:
        return 'Hello!'
    else:
        return f'Hello {name}!'

@app.route('/api_endpoint_cuong')
def api_endpoint():
    # Simulating data retrieval from the API
    try:
        # Code to fetch data from the API
        data = {"message": "Data fetched successfully from the API"}
        return jsonify(data), 200
    except Exception as e:
        # Handle any errors that occur during data retrieval
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = find_free_port()
    print(f'Free port found: {port}')
    app.run(host='0.0.0.0', port=port)  # Run the app on the dynamically assigned port
