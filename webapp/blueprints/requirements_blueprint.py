import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, render_template, request, redirect, url_for, flash
import database.db_utils as db_utils
from database.insert_data import SchedulingDB

requirements = Blueprint('requirements', __name__)
scheduling_db = SchedulingDB('scheduling.db')

@requirements.route('/requirements', methods=['GET', 'POST'])
def manage_requirements():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_with_indices = list(enumerate(days))
    message = ""

    if request.method == 'POST':
        # Update shift requirements based on the form data
        for day_idx, _ in days_with_indices:
            for shift_idx in range(9):  # Assuming you have 9 shifts per day
                input_name = f"requirement_{day_idx}_{shift_idx}"
                new_requirement = request.form.get(input_name)
                if new_requirement is not None:
                    scheduling_db.update_shift_requirement(day_idx, shift_idx, int(new_requirement))
        message = "Shift requirements updated successfully."
        # Optional: You can use flash() instead of passing a message
        # flash("Shift requirements updated successfully.")

    # Fetch shift requirements from the database for displaying
    all_shift_requirements = db_utils.fetch_all_shift_requirements()
    shift_requirements = [[0] * 9 for _ in range(7)]  # Initialize matrix for 7 days and 9 shifts
    for day, shift, count in all_shift_requirements:
        shift_requirements[day][shift] = count

    return render_template('requirements/requirements_manage.html', 
                           shift_requirements=shift_requirements, 
                           days=days_with_indices, 
                           message=message)
