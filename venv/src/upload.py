from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# bad idea to have GET and POST in the same route, but there are exceptions
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            uploaded_file.save(uploaded_file.filename)
            return "file uploaded successfully"
        return redirect(url_for("index"))
    return render_template("index.html")


"""
@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'
"""

if __name__ == "__main__":
    app.run(debug=True)
