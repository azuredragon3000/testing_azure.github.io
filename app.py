from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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
    app.run(debug=True, port=5001)
