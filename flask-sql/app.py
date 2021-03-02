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

#データベースの仕様
class order_table(db.Model):
    orderid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    goods_number = db.Column(db.Integer)
    payment = db.Column(db.Text())

    #プライマリキー
    def __init__(self, pub_date, goods_number, payment):
        self.pub_date = pub_date
        self.goods_number = goods_number
        self.payment = payment

# テーブル作成
# db.create_all()
# print('ok')


#INSERT
# データ1
# date = datetime.now()
# goods_number = 810
# payment = 'cash'

# データ2
# date = datetime.now()
# goods_number = 811
# payment = "credit"

# データ3
# date2 = datetime.now()
# goods_number2 = 812
# payment2 = "credit"

#データ追加
# add_data = order_table(date, goods_number, payment)
# add_data = order_table(date, goods_number, payment)
# add_data2 = order_table(date2, goods_number2, payment2)

# db.session.add(add_data)
# db.session.add(add_data)
# db.session.add(add_data2)

#変更保存
# db.session.commit()


#SELECT
#データ読込
# order = order_table.query.all()

#表示
# print(order, type(order))
# print(dir(order[0]))
# print(order[0].pub_date, order[0].goods_number, order[0].payment)

#取得
# goodsdata = []
# for i in order:
#     goodsdata.append(i.goods_number)

#中身表示
# print(goodsdata)


#WHERE
# order = order_table.query.filter_by(goods_number=811).first()
# print(order)
# print(order.orderid,order.goods_number,order.pub_date)


#UPDATE
# order = order_table.query.filter_by(goods_number=811).first()
# order.goods_number = 850
# db.session.commit()
# print(order.orderid, order.goods_number, order.pub_date)


#DROP
order = order_table.query.filter_by(goods_number=810).first()
db.session.delete(order)
db.session.commit()

# sqlite－初心者向け
# Sqlalchemy－中級者以降向け
