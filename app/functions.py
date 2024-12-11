import os.path
import secrets

from flask import current_app


def save_image(pic):
    if pic:
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(pic.filename)
        picture_file_name = random_hex + f_ext
        picture_path = os.path.join(current_app.config["SERVER_PATH"], picture_file_name)
        pic.save(picture_path)
        return picture_file_name
    else:
        return None


