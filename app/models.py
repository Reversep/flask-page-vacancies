from . import db


class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String(20))
    address = db.Column(db.String(25))
    data_open = db.Column(db.Date)


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position_name = db.Column(db.String(20))
    department = db.Column(db.String(25))


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    phone_number = db.Column(db.Integer)
    data_birth = db.Column(db.Date)
    data_in = db.Column(db.Date)
    data_out = db.Column(db.Date)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)
    branch = db.relationship('Branch', backref=db.backref('branchs', lazy='dynamic'))
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    position = db.relationship('Position', backref=db.backref('positions', lazy='dynamic'))
