import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, render_template, request, redirect, url_for
import database.db_utils as db_utils
from database.insert_data import SchedulingDB

employees = Blueprint('employees', __name__)
scheduling_db = SchedulingDB('scheduling.db')

@employees.route('/view')
def view():
    data = db_utils.fetch_all_employees()
    return render_template('employees/employee_view.html', data=data)

@employees.route('/add', methods=['GET'])
def add_employee_form():
    # This route only handles the GET request to display the form
    return render_template('employees/employee_add.html')

@employees.route('/add', methods=['POST'])
def add_employee():
    # Get the form data
    employee_name = request.form['employee_name']
    # Insert into the database (using your custom function)
    scheduling_db = SchedulingDB('scheduling.db')
    # Insert into the database
    try:
        scheduling_db.insert_employee(employee_name)
        return redirect(url_for('employees.view'))
    except Exception as e:
        # Log the exception
        print(f"An error occurred: {e}")
        return "Error adding employee", 500

@employees.route('/edit/<int:employee_id>', methods=['GET'])
def edit_employee_form(employee_id):
    # Fetch the current data of the employee
    employee_data = db_utils.fetch_employee_by_id(employee_id)
    if employee_data:
        return render_template('employees/employee_edit.html', employee=employee_data)
    else:
        return "Employee not found", 404

@employees.route('/edit/<int:employee_id>', methods=['POST'])
def update_employee(employee_id):
    # Get the form data
    new_name = request.form['employee_name']
    # Update in the database (using your custom function)
    try:
        scheduling_db.update_employee_name(employee_id, new_name)
        return redirect(url_for('employees.view'))
    except Exception as e:
        # Log the exception
        print(f"An error occurred: {e}")
        return "Error updating employee", 500

@employees.route('/delete/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    try:
        scheduling_db.delete_employee(employee_id)
        return redirect(url_for('employees.view'))
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error deleting employee", 500