from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class Employer(db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.String(11), primary_key=True, unique=True, default =get_uuid)
    email = db.Column(db.String(150), unique=True)
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    password = db.Column(db.Text, nullable=False)
    # Define relationships with User table
    user_id = db.Column(db.String(11), db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='employee')

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    employer_email = db.Column(db.String(255), nullable=False)
    employee_email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Hashed password


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(11), primary_key=True, unique=True, default =get_uuid)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.Text, nullable=False)




#All db models

#Employer Model (for Manager)
# Relationship: One-to-One with User (Foreign Key: user_id)
# Relationship: One-to-Many with Employee (via employer_id)
class Employer(db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.String(11), primary_key=True, unique=True, default=get_uuid)
    email = db.Column(db.String(150), unique=True)
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    password = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String(11), db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='employer')
    employees = db.relationship('Employee', back_populates='employer', cascade='all, delete-orphan')

#Employee Model, Relationship: Many-to-One with Employer (Foreign Key: employer_id)
class Employee(db.Model):
    id = db.Column(db.String(11), primary_key=True, unique=True, default=get_uuid)
    employee_email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # position = db.Column(db.String(100), nullable=False)
    # seniority = db.Column(db.Integer, nullable=False)
    employer_id = db.Column(db.String(11), db.ForeignKey('employers.id'), nullable=False)
    employer = db.relationship('Employer', back_populates='employees')


## Defining the many-to-many relationship table Between Schedule and Shift Tables
schedule_shifts = db.Table(
    'schedule_shifts',
    db.Column('schedule_id', db.String(11), db.ForeignKey('schedule.id'), primary_key=True),
    db.Column('shift_id', db.String(11), db.ForeignKey('shift.id'), primary_key=True)
)


# Defining the many-to-many relationship table Between Shifts and employees
employee_shifts = db.Table(
    'employee_shifts',
    db.Column('employee_id', db.String(11), db.ForeignKey('employee.id'), primary_key=True),
    db.Column('shift_id', db.String(11), db.ForeignKey('shift.id'), primary_key=True)
)

# Shift Model
# Relationship: Many-to-Many with Employee (via employee_shifts table)
# Relationship: Many-to-Many with Schedule (via schedule_shifts table)
class Shift(db.Model):
    id = db.Column(db.String(11), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    employees = db.relationship('Employee', secondary=employee_shifts, back_populates='shifts')
    schedules = db.relationship('Schedule', secondary=schedule_shifts, back_populates='shifts')

#
# Schedule Model
# Relationship: Many-to-One with Employer (Foreign Key: employer_id)
# Relationship: Many-to-Many with Shift (via schedule_shifts table)
# Relationship: One-to-Many with Availability (via schedule_id)
# Relationship: One-to-Many with Notification (via schedule_id)
class Schedule(db.Model):
    id = db.Column(db.String(11), primary_key=True, unique=True, default=get_uuid)
    week_start_date = db.Column(db.Date, nullable=False)
    employer_id = db.Column(db.String(11), db.ForeignKey('employers.id'), nullable=False)
    employer = db.relationship('Employer', back_populates='schedules')
    shifts = db.relationship('Shift', secondary=schedule_shifts, back_populates='schedules')
    availabilities = db.relationship('Availability', back_populates='schedule', cascade='all, delete-orphan')
    notifications = db.relationship('Notification', back_populates='schedule', cascade='all, delete-orphan')


# Availability Model
class Availability(db.Model):
    id = db.Column(db.String(11), primary_key=True, unique=True, default=get_uuid)
    employee_id = db.Column(db.String(11), db.ForeignKey('employees.id'), nullable=False)
    employee = db.relationship('Employee', back_populates='availabilities')
    schedule_id = db.Column(db.String(11), db.ForeignKey('schedules.id'), nullable=False)
    schedule = db.relationship('Schedule', back_populates='availabilities')
    permanent_availability = db.Column(db.JSON)
    temporary_availability = db.Column(db.JSON)

# Notification Model
class Notification(db.Model):
    id = db.Column(db.String(11), primary_key=True, unique=True, default=get_uuid)
    schedule_id = db.Column(db.String(11), db.ForeignKey('schedules.id'), nullable=False)
    schedule = db.relationship('Schedule', back_populates='notifications')
    employee_id = db.Column(db.String(11), db.ForeignKey('employees.id'), nullable=False)
    employee = db.relationship('Employee', back_populates='notifications')
    message = db.Column(db.Text)
    status = db.Column(db.String(20), default='Unread')


#Shift Preference Model
class ShiftPreferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    day_of_week = db.Column(db.Integer, nullable=False)
    shift_id = db.Column(db.Integer, nullable=False)
    preference_score = db.Column(db.Integer, nullable=False)
