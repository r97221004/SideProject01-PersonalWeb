from datetime import datetime
from PersonalWeb import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default = datetime.utcnow, index = True )


# utcnow 表示現在的世界協調時間
# 在這裡不要加括號 
# index = True 表示在這欄位加索引，這樣在搜索 timestamp 時會變快
    