from flask_admin.form.upload import FileUploadField, ImageUploadField
from src.admin_views.base import SecureModelView
from flask import current_app

class LetterView(SecureModelView):
    form_overrides = {
        "image": ImageUploadField,
        "sound": FileUploadField
    }

    form_args = {
        "image": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/"
        },
        "sound": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "sounds/"
        }
    }