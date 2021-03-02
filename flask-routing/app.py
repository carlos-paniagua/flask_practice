from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)


# http://xxx 以降のURLパスを '/' と指定

#トップ画面
@app.route("/")
def index():
  return render_template("index.html")

@app.route('/members')
def user_url():
    lists = [[1, "太郎"], [2, "次郎"], [3, "三郎"]]
    return render_template("member.html", lists=lists)


@app.route("/member_detail/<int:id_>/<name>")
def detail(id_,name):
    lists = [['太郎',24,'サッカー'], ['次郎',45,'野球'], ['三郎',67,'バスケ']]
    index = id_-1
    data = lists[index]
    return render_template("detail.html", data=data, name=name)


#リダイレクト処理
@app.route('/redirects')
def redirects():
    return redirect(url_for('index')) # url_for('送信先の関数名',送信するデータ)


app.run(debug=True)
