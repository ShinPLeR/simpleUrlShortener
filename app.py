import os
import re
import os
from typing import Optional

from dotenv import load_dotenv
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, URLField

load_dotenv(".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"


@app.route("/", methods=["GET", "POST"])
def hello_world():
    form = Form()
    if request.method == "GET":
        return render_template("index.html", form=form)
    else:
        if form.validate_on_submit():
            return render_template("index.html", form=form)
        else:
            return render_template("index.html", form=form)


def generate_shortened_url(url: str, arbitrary_id: Optional[str]) -> str:
    """
    Generate shortened url
    :param url:
    :param arbitrary_id:
    :return:
    """

    return ""


class Form(FlaskForm):
    original_url = URLField(label="元URL")
    arbitrary_id = StringField(label="任意の文字列")

    def validate_url(self, original_url):
        if original_url.data == "":
            raise ValidationError("元のURLを入力してください")
        if not re.match(url_pattern, original_url.data):
            raise ValidationError("URLの形式が違います")
        if len(original_url.data) > 1000:
            raise ValidationError("使用可能なURLは1000文字までです")

    def validate_arbitrary_id(self, arbitrary_id):
        if arbitrary_id.data is not None and len(arbitrary_id.data) > 15:
            raise ValidationError("IDとして設定できる文字列は15文字以内です")


if __name__ == '__main__':
    app.run(debug=os.environ.get("APP_ENV") != "production")
