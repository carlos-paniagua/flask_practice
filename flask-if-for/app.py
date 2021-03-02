# Flask呼び出し
from flask import Flask, render_template

# クラス呼び出し
app = Flask(__name__)


# ルーティング設定
@app.route('/')
def hello_World():
    return 'HelloWorld！'

@app.route('/title')
def title():
    return render_template("index.html")


@app.route('/jinja_test')
def jinja_test():
    return render_template("jinja_test.html",name="carlos")


@app.route('/test_if1')
def test_if1(name=None):
  name = "nobuto"
  return render_template("test_if.html", name=name)

@app.route('/test_if2')
def test_if2(name=None):
  name = "carlos"
  return render_template("test_if.html", name=name)

@app.route('/test_for')
def test_for():
  man = ["足利","岩田","隆平"]
  return render_template("test_for.html", name=man)
  

# サーバー起動
if __name__ == "__main__":
    app.run(debug=True)
