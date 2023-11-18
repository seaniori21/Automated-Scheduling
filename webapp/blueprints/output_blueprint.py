import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, render_template, request, redirect, url_for, flash
import database.db_utils as db_utils
from database.insert_data import SchedulingDB
from base import Scheduler, get_input_data

output = Blueprint('output', __name__)

@output.route('/output')
def show_schedule():
    # Fetch the input data needed for the scheduler
    employee_data, shift_data, preferences, seniority, shift_requirements = get_input_data()

    # Initialize the scheduler with the fetched data
    scheduler = Scheduler(employee_data, shift_data, preferences, seniority, shift_requirements)

    # Generate the schedule
    schedule, total_shifts_per_employee = scheduler.generate_schedule()

    # Pass the schedule to the template
    return render_template('schedule.html', schedule=schedule, total_shifts=total_shifts_per_employee)