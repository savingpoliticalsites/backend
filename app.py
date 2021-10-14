from flask import Flask
from config import db_uri

app = Flask(__name__)

@app.route("/form", methods=["GET", "POST"])
def form():
    pass

