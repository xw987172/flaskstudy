from flask import Flask,render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/')
def index():
    return render_template('first_app.html')

if __name__ == '__main__':
    app.run()
