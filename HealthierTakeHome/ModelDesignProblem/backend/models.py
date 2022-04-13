from backend import db


class Wombat(db.Model):
    __tablename__ = 'wombats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    dob = db.Column(db.Date)

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return f"<Wombat {self.name}, born: {self.dob}>"

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'dob': self.dob.isoformat()
        }
        return data
