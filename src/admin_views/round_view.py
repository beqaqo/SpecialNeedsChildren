from flask_admin.form.upload import FileUploadField, ImageUploadField
from src.admin_views.base import SecureModelView
from flask import current_app
from markupsafe import Markup


class RoundView(SecureModelView):
    form_overrides = {
        "image": ImageUploadField
    }

    form_args = {
        "image": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/"
        }
    }
    def image_formatter(self, context, model, name):
        if model.image:
            return Markup(f"<img src='/static/assets/{model.image}' width = '100' >")

    column_formatters = {
        "image": image_formatter
    }