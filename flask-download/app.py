from flask import Flask, send_from_directory,render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/export")
def export_action():
  path = os.path.abspath(__file__)[:-7]
  return send_from_directory(
    directory=path + "\export_temp",
    filename="test.csv",
    as_attachment=True,
    attachment_filename="test.csv"
  )

app.run(debug=True)
  