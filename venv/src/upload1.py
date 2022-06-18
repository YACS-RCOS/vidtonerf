import imghdr
from io import BytesIO
import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    abort,
    send_from_directory,
)
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 2 << 19  # 1MB (1024*1024)? why?
app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png", ".gif"]
app.config["UPLOAD_PATH"] = "uploads"


def validate_image(stream: BytesIO) -> bool:
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)

    # Invalid header means None,
    # otherwise append the filetype, except jpeg file "types" should end in .jpg NOT .jpeg
    return bool(format)


@app.route("/")
def index():
    files = os.listdir(app.config.get("UPLOAD_PATH"))
    return render_template("index.html", files=files)

# shouldn't be /
@app.route("/", methods=["POST"])
def upload_files():
    uploaded_file = request.files.get("file")
    filename = secure_filename(uploaded_file.filename)

    # what about if not filename?
    if filename:
        file_ext = os.path.splitext(filename)[-1]
        # sometimes there can be multiple dots, better to get the last one
        if not validate_image(uploaded_file.stream) or file_ext not in app.config.get(
            "UPLOAD_EXTENSIONS"
        ):
            abort(400)
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))
    return redirect(url_for("index"))


# this is likely just you testing around but we should not be submitting the filename in the url, bad practice
@app.route("/uploads/<filename>")
def upload(filename):
    return send_from_directory(app.config["UPLOAD_PATH"], filename)
