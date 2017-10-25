import os
from io import BytesIO
from pymongo import MongoClient
from PIL import Image
import requests


def open_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.filename = os.path.basename(url)
    return image


def resize_image(image, new_size):
    new_image = image.resize(new_size, Image.ANTIALIAS)
    return new_image


def append_suffix_to_filename(filename, suffix):
    filename_split = filename.split(".")
    filename_split[0] += suffix
    return ".".join(filename_split)


def run(given_endpoint, host, mongodb_uri):

    # Setup Mongo
    mongo_client = MongoClient(mongodb_uri)
    db = mongo_client.get_database()

    # Clearing previously URL registers
    db.photos.remove({}, {"justOne": False})

    # Get images URLs
    response = requests.get(given_endpoint)
    urls = [image["url"] for image in response.json()["images"]]

    for url in urls:
        # Opening image from URL
        original_img = open_image_from_url(url)

        # Resizing image
        small_img = resize_image(original_img, (320, 240))
        medium_img = resize_image(original_img, (384, 288))
        large_img = resize_image(original_img, (640, 480))

        # Renaming files
        small_img_filename = append_suffix_to_filename(original_img.filename, "_small")
        medium_img_filename = append_suffix_to_filename(original_img.filename, "_medium")
        large_img_filename = append_suffix_to_filename(original_img.filename, "_large")

        # Saving files
        small_img.save("static/images/{}".format(small_img_filename))
        medium_img.save("static/images/{}".format(medium_img_filename))
        large_img.save("static/images/{}".format(large_img_filename))

        # Saving URLs reference on DB
        db.photos.insert({
            "small": {"url": "{}/images/{}".format(host, small_img_filename)},
            "medium": {"url": "{}/images/{}".format(host, medium_img_filename)},
            "large": {"url": "{}/images/{}".format(host, large_img_filename)}
        })
