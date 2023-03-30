from datetime import date

import wtforms as wtf
from flask_wtf import FlaskForm

from . import app
from .models import Branch, Position


def validate_branch_open_date(form, open_date):
    today = date.today()
    if open_date.data > today:
        raise ValueError("Филиал не может быть открыт позже сегодняшнего дня")


class BranchForm(FlaskForm):
    branch_name = wtf.StringField(label='Название филиала', validators=[
        wtf.validators.Regexp('[^0-9!@#$%^&*]*')
    ])
    address = wtf.StringField(label='Адрес')
    date_open = wtf.DateField('Дата открытия', validators=[
        validate_branch_open_date
    ])



class PositionForm(FlaskForm):
    position_name = wtf.StringField(label='Название должности', validators=[
        wtf.validators.Regexp('[^0-9!@#$%^&*]*')
    ])
    department = wtf.StringField(label='Отделение', validators=[
        wtf.validators.Regexp('[^0-9!@#$%^&*]*', message='не должно быть спецсимволов таких как «!@#$%^&*»')
    ])


def branch_choices():
    br_choices = []
    with app.app_context():
        branchs = Branch.query.all()
        for br in branchs:
            br_choices.append((br.id, br.branch_name))
    return br_choices


def position_choices():
    p_choices = []
    with app.app_context():
        positions = Position.query.all()
        for pos in positions:
            p_choices.append((pos.id, pos.position_name))
    return p_choices


def validate_age(form, field):
    date_in = form.data_in.data
    date_birth = field.data
    age = (date_in - date_birth).days // 365
    if age < 18:
        raise wtf.ValidationError("Сотруднику должно быть 18 и более лет")

def validate_date_out(form, field):
    date_in = form.data_in.data
    date_out = field.data
    if date_out < date_in:
        raise wtf.ValidationError("Дата увольнения не может быть раньше даты принятия на работу")


class EmployeeForm(FlaskForm):
    full_name = wtf.StringField(label='ФИО работника', validators=[
        wtf.validators.Regexp('[^0-9!@#$%^&*]*')
    ])
    phone_number = wtf.IntegerField(label='Номер телефона')
    data_birth = wtf.DateField('Дата рождения', validators=[
        validate_age
    ])
    data_in = wtf.DateField(label='Дата трудоустройства', validators=[
    ])
    data_out = wtf.DateField(label='Дата увольнения', validators=[
        validate_date_out
    ])
    branch_id = wtf.SelectField(label='Филиал', choices=branch_choices)
    position_id = wtf.SelectField(label='Должность', choices=position_choices)
