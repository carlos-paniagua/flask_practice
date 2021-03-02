from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemyでデータベースに接続する
db_uri = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

class Comment(db.Model):
  id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
  pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  name = db.Column(db.Text())
  comment = db.Column(db.Text())

  def __init__(self, pub_date, name, comment):
    self.pub_date = pub_date
    self.name = name
    self.comment = comment


try:
  db.create_all()
except Exception as e:
  print(e.args)
  pass

@app.route("/")
def index():
  text = Comment.query.all()
  return render_template("index.html",lines=text)


@app.route("/result",methods=["POST"])
def result():
  date = datetime.now()
  comment = request.form["comment_data"]
  name = request.form["name"]
  comment_data = Comment(pub_date=date, name=name, comment=comment)
  db.session.add(comment_data)
  db.session.commit()
  return render_template("result.html",comment=comment,name=name,now=date)


if __name__ == "__main__":
    app.run(debug=True)
