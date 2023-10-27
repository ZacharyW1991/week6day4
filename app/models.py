from app import db
from datetime import datetime

class Address(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String, nullable=False)
    last_name=db.Column(db.String, nullable=False)
    phone=db.Column(db.String, nullable=False)
    address=db.Column(db.String, nullable=False)
    date_created=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'phone':self.phone,
            'address':self.address,
            'date_created':self.date_created
        }