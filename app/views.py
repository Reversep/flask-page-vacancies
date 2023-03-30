from flask import request, render_template, url_for, redirect
from . import app, db

from .models import Branch, Position, Employee
from .forms import BranchForm, PositionForm, EmployeeForm


def branch_list():
    branchs = Branch.query.all()
    return render_template('branch_view.html', branchs=branchs)


def position_list():
    positions = Position.query.all()
    return render_template('position_view.html', positions=positions)


def employee_list():
    employees = Employee.query.all()
    return render_template('employee_view.html', employees=employees)


def branch_add():
    form = BranchForm(meta={'csrf': False})
    if request.method == 'POST':
        if form.validate_on_submit():
            new_branch = Branch(
                branch_name=form.branch_name.data,
                address=form.address.data,
                data_open=form.date_open.data
            )
            db.session.add(new_branch)
            db.session.commit()
            return redirect(url_for('branch_list'))
        else:
            print(form.errors)
    return render_template('branch_add.html', form=form)


def position_add():
    form = PositionForm(meta={'csrf': False})
    if request.method == 'POST':
        if form.validate_on_submit():
            new_position = Position(
                position_name=form.position_name.data,
                department=form.department.data
            )
            db.session.add(new_position)
            db.session.commit()
            return redirect(url_for('position_list'))
        else:
            print(form.errors)
    return render_template('position_add.html', form=form)


def employee_add():
    form = EmployeeForm(meta={'csrf': False})
    if request.method == 'POST':
        if form.validate_on_submit():
            new_employee = Employee(
                full_name=form.full_name.data,
                phone_number=form.phone_number.data,
                data_birth=form.data_birth.data,
                data_in=form.data_in.data,
                data_out=form.data_out.data,
                branch_id=form.branch_id.data,
                position_id=form.position_id.data
            )
            db.session.add(new_employee)
            db.session.commit()
            return redirect(url_for('employee_list'))
        else:
            print(form.errors)
    return render_template('employee_add.html', form=form)
