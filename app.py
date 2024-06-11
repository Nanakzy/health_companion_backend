from flask import Flask
from routes import get_features

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
