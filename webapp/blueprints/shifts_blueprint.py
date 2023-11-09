import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, render_template, request, redirect, url_for
import database.db_utils as db_utils
from database.insert_data import SchedulingDB

shifts = Blueprint('shifts', __name__)
scheduling_db = SchedulingDB('scheduling.db')

@shifts.route('/view')
def view_shifts():
    data = db_utils.fetch_all_shifts()
    return render_template('shifts/shift_view.html', data=data)

@shifts.route('/add', methods=['GET'])
def add_shift_form():
    # This route only handles the GET request to display the form
    return render_template('shifts/shift_add.html')

@shifts.route('/add', methods=['POST'])
def add_shift():
    # Get the form data
    shift_name = request.form['shift_name']
    # Insert into the database
    try:
        scheduling_db.insert_shift(shift_name)
        return redirect(url_for('shifts.view_shifts'))
    except Exception as e:
        # Log the exception
        print(f"An error occurred: {e}")
        return "Error adding employee", 500

@shifts.route('/edit/<int:shift_id>', methods=['GET'])
def edit_shifts_form(shift_id):
    # Fetch the current data of the employee
    shifts_data = db_utils.fetch_shifts_by_id(shift_id)
    if shifts_data:
        return render_template('shifts/shift_edit.html', shift=shifts_data)
    else:
        return "Employee not found", 404

@shifts.route('/edit/<int:shift_id>', methods=['POST'])
def update_shifts(shift_id):
    # Get the form data
    new_shifts = request.form['shift_name']
    # Update in the database (using your custom function)
    try:
        scheduling_db.update_shift_name(shift_id, new_shifts)
        return redirect(url_for('shifts.view_shifts'))
    except Exception as e:
        # Log the exception
        print(f"An error occurred: {e}")
        return "Error updating employee", 500

@shifts.route('/delete/<int:shift_id>', methods=['POST'])
def delete_shift(shift_id):
    try:
        scheduling_db.delete_shift(shift_id)
        return redirect(url_for('shifts.view_shifts'))
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error deleting employee", 500
