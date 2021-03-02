# Flaskを使ってページ表示
## app.py
### app = Flask(__name__)
 flask モジュールが提供している Flask クラスを利用

### @app.route('/')
デコレータ
次の行で定義される関数を指定した URL にマッピングする

### @app.route('/hello')
http://127.0.0.1:5000/hello にアクセス

### app.run(debug=True)
Flask が持っている開発用サーバーを、 デバッグモードで実行


## jinja_test.html
### {{パラメータ名}}
波括弧を二重にして囲むことで、テンプレートの中に.py側から渡した値を書き出すことができる


## test_if.html
### {% if %}～{% else %}～{% endif %}

## test_for.html
### {% for  in %}～{% endfor %}