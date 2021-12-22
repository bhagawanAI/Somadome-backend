from db import db


class Img(db.Model):
    # id = db.Column(db.Integer,primary_key=True)
    # entityType = db.Column(db.Text)
    #
    # entityId = db.Column(db.Integer)
    # replace = db.Column(db.Boolean)
    # index = db.Column(db.Integer)
    # imageData = db.Column(db.Text)
    # name = db.Column(db.Text, nullable=False)
    # mimetype = db.Column(db.Text, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    entityType = db.Column(db.Text)
    entityId = db.Column(db.Integer)
    replace = db.Column(db.Boolean)
    index = db.Column(db.Integer)
    imageData = db.Column(db.Text, unique=True, nullable=False)
    # name = db.Column(db.Text, nullable=False)
    # mimetype = db.Column(db.Text, nullable=False)