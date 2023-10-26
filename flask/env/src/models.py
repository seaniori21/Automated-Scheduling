from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex


# User Model: Used to store user information, such as email and password.
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.Text, nullable=False)

# Employer Model: Represents employer information and relationships with employees.
class Employer(db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    email = db.Column(db.String(150), unique=True)
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    password = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String(32), db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='employer')
    employees = db.relationship('Employee', back_populates='employer', cascade='all, delete-orphan')

# Employee Model: Represents employee information and relationships with employers.
class Employee(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    employee_email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    employer_id = db.Column(db.String(32), db.ForeignKey('employers.id'), nullable=False)
    employer = db.relationship('Employer', back_populates='employees')

# schedule_shifts and employee_shifts: Define many-to-many relationships between Shifts, Employees, and Schedules.
# These tables represent the shifts assigned to employees in different schedules.

schedule_shifts = db.Table(
    'schedule_shifts',
    db.Column('schedule_id', db.String(32), db.ForeignKey('schedule.id'), primary_key=True),
    db.Column('shift_id', db.String(32), db.ForeignKey('shift.id'), primary_key=True)
)

employee_shifts = db.Table(
    'employee_shifts',
    db.Column('employee_id', db.String(32), db.ForeignKey('employee.id'), primary_key=True),
    db.Column('shift_id', db.String(32), db.ForeignKey('shift.id'), primary_key=True)
)


# Shift Model: Represents shift information and relationships with employees and schedules.
class Shift(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    employees = db.relationship('Employee', secondary=employee_shifts, back_populates='shifts')
    schedules = db.relationship('Schedule', secondary=schedule_shifts, back_populates='shifts')


# Schedule Model: Represents schedule information and relationships with employers, shifts, availabilities, and notifications.
class Schedule(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    week_start_date = db.Column(db.Date, nullable=False)
    employer_id = db.Column(db.String(32), db.ForeignKey('employers.id'), nullable=False)
    employer = db.relationship('Employer', back_populates='schedules')
    shifts = db.relationship('Shift', secondary=schedule_shifts, back_populates='schedules')
    availabilities = db.relationship('Availability', back_populates='schedule', cascade='all, delete-orphan')
    notifications = db.relationship('Notification', back_populates='schedule', cascade='all, delete-orphan')


# Availability Model: Represents employee availability and relationships with employees and schedules.
class Availability(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    employee_id = db.Column(db.String(32), db.ForeignKey('employee.id'), nullable=False)
    employee = db.relationship('Employee', back_populates='availabilities')
    schedule_id = db.Column(db.String(32), db.ForeignKey('schedule.id'), nullable=False)
    schedule = db.relationship('Schedule', back_populates='availabilities')
    permanent_availability = db.Column(db.JSON)
    temporary_availability = db.Column(db.JSON)


# Notification Model: Represents notifications and relationships with employees and schedules.
class Notification(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    schedule_id = db.Column(db.String(32), db.ForeignKey('schedule.id'), nullable=False)
    schedule = db.relationship('Schedule', back_populates='notifications')
    employee_id = db.Column(db.String(32), db.ForeignKey('employee.id'), nullable=False)
    employee = db.relationship('Employee', back_populates='notifications')
    message = db.Column(db.Text)
    status = db.Column(db.String(20), default='Unread')


# ShiftPreferences Model: Represents employee shift preferences.
class ShiftPreferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(32), db.ForeignKey('employee.id'), nullable=False)
    day_of_week = db.Column(db.Integer, nullable=False)
    shift_id = db.Column(db.String(32), nullable=False)
    preference_score = db.Column(db.Integer, nullable=False)


# EmployeeInvited Model: Used to ensure that employees are invited by their employers during the signup process.
class EmployeeInvited(db.Model):
    __tablename__ = 'employee_invited'
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    employer_id = db.Column(db.String(32), db.ForeignKey('employers.id'), nullable=False)
    employer_email = db.Column(db.String(150), nullable=False)
    employee_email = db.Column(db.String(255), unique=True, nullable=False)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    employer = db.relationship('Employer', back_populates='invitations')



# class Employer(db.Model):
#     __tablename__ = 'employers'
#     id = db.Column(db.String(11), primary_key=True, unique=True, default =get_uuid)
#     email = db.Column(db.String(150), unique=True)
#     firstname = db.Column(db.String(150), nullable=False)
#     lastname = db.Column(db.String(150), nullable=False)
#     company = db.Column(db.String(150), nullable=False)
#     password = db.Column(db.Text, nullable=False)
#     # Define relationships with User table
#     user_id = db.Column(db.String(11), db.ForeignKey('users.id'), nullable=False)
#     user = db.relationship('User', back_populates='employee')
#
# class Employee(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     company_name = db.Column(db.String(255), nullable=False)
#     employer_email = db.Column(db.String(255), nullable=False)
#     employee_email = db.Column(db.String(255), unique=True, nullable=False)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     password = db.Column(db.String(60), nullable=False)  # Hashed password

