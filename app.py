from flask import Flask, jsonify, render_template
from configparser import ConfigParser
from pymongo import MongoClient
import photos_resizer
import uwsgi


given_endpoint = uwsgi.opt["given_endpoint"]
host = uwsgi.opt["host"]
mongodb_uri = uwsgi.opt["mongodb_uri"]

photos_resizer.run(given_endpoint, host, mongodb_uri)

app = Flask(__name__)


@app.route("/")
def index():
    mongo_client = MongoClient(uwsgi.opt["mongodb_uri"])
    db = mongo_client.get_database()

    images_info = {
        "images": [
        ]
    }

    for photo_group in db.photos.find():
        del photo_group["_id"]
        images_info["images"].append(photo_group)
        print images_info["images"]

    return jsonify(images_info)


@app.route("/images/<image_name>")
def show_image(image_name):
    return render_template("image.html", image_name=image_name)
