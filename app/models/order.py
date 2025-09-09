from sqlalchemy.sql.functions import now

from .. import db


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    order_name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=now())
