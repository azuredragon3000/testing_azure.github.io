from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    abc = "example_value"
    return render_template('index.html',abc=abc)

if __name__ == '__main__':
    app.run(debug=True)
