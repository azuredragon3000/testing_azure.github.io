import socket
from flask import Flask, render_template, jsonify

app = Flask(__name__)

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

@app.route('/api_endpoint')
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
    app.run(debug=True, port=port)
