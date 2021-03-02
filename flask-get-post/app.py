from flask import Flask, render_template, request

app = Flask(__name__)

#トップ画面
@app.route("/")
def index():
  return render_template("index.html")

#GET入力フォーム
@app.route("/request_get")
def get():
  return render_template("send_get.html")

#GET処理
@app.route("/receive_get", methods=["GET"])
def receive_get():
  name = request.args["my_name"]
  if len(name) == 0:
    return "名前が未入力"
  else:
    return "あなたの入力した名前は" + str(name) + "です"

#POST入力フォーム
@app.route("/request_post", methods=["GET"])
def post_smaple():
  return render_template("send_post.html")

#POST処理
@app.route("/request_post", methods=["POST"])
def post_action():
  if "gender" in request.form.keys():
    gender = request.form["gender"]
    if gender == "男":
      sex = "男性"
    elif gender == "女":
      sex = "女性"
  else:
    sex = "性別不明"
  if "age" in request.form.keys():
    age_range = request.form["age"]
  else:
    age_range = "年齢不詳"
  return f'あなたは{sex}で{age_range}です。'

# サーバー起動
if __name__ == "__main__":
    app.run(debug=True)
'''
GET リクエストの場合なら request.args()
POSTリクエストの場合なら request.form()
value=””に指定した値が、request.argsまたはrequest.form
'''

