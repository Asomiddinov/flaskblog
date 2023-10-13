from __init__ import db, login_manager
from wtforms import IntegerField, FloatField, StringField, TextAreaField, SearchField, SubmitField, SelectField, DateField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from flask_login import UserMixin
from datetime import datetime


class Clients(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, fullname, email):
        self.fullname = fullname
        self.email = email


class Mine(FlaskForm):
    id = IntegerField()
    fullname = StringField("Name of place",
                           validators=[DataRequired("!!!")])
    email = StringField("Description", validators=[DataRequired()])
    submit = SubmitField("🆗")


class Posts(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    patient = db.Column(db.String, nullable=False)
    pat_code = db.Column(db.String, nullable=False)
    pat_code1 = db.Column(db.String, nullable=False)
    pat_code2 = db.Column(db.String, nullable=False)
    pat_code3 = db.Column(db.String, nullable=False)
    pat_code4 = db.Column(db.String, nullable=False)
    pat_code5 = db.Column(db.String, nullable=False)
    pat_code6 = db.Column(db.String, nullable=False)
    pat_code7 = db.Column(db.String, nullable=False)
    pat_code8 = db.Column(db.String, nullable=False)
    pat_code9 = db.Column(db.String, nullable=False)
    pat_code10 = db.Column(db.String, nullable=False)
    pat_code11 = db.Column(db.String, nullable=False)
    pat_code12 = db.Column(db.String, nullable=False)
    pat_code13 = db.Column(db.String, nullable=False)
    pat_code14 = db.Column(db.String, nullable=False)
    pat_code15 = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'''Posts({self.id}, '{self.date}', {self.patient},
        {self.pat_code}, {self.pat_code1}, {self.pat_code2}, {self.pat_code3}, {self.pat_code4}, {self.pat_code5}, {self.pat_code6},
        {self.pat_code7}, {self.pat_code8}, {self.pat_code9}, {self.pat_code10}, {self.pat_code11}, {self.pat_code12}, {self.pat_code13},
        {self.pat_code14}, {self.pat_code15})'''


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    comment = db.Column(db.String)
    role = db.Column(db.String)
