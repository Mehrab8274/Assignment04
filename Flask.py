from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

@app.route('/about')
def about():
    return 'This is a simple Flask web application.'


if __name__ == '__main__':
    app.run()
