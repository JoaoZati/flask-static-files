from flask import Flask, render_template
from second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="")


@app.route('/')
def home():
    return '<h1>TEST</h1>'


if __name__ == '__main__':
    app.run(debug=True)
