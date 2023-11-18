import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'scheduling.db')

def create_connection():
    """Create a database connection and return the connection object."""
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

def create_connection():
    """Create a database connection and return the connection object."""
    connection = sqlite3.connect('scheduling.db')
    return connection

def fetch_all_employees():
    """Fetch all employees from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    conn.close()
    return employees

def fetch_employee_by_id(employee_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
    employee = cursor.fetchone()
    conn.close()

    return employee

def fetch_all_shifts():
    """Fetch all shifts from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shifts")
    shifts = cursor.fetchall()
    conn.close()
    return shifts

def fetch_shifts_by_id(shift_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shifts WHERE id = ?", (shift_id,))
    shifts = cursor.fetchone()
    conn.close()
    return shifts

def fetch_all_unavailable_days():
    """Fetch all unavailable days from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM unavailabledays")
    unavailable_days = cursor.fetchall()
    conn.close()
    return unavailable_days

def fetch_all_shift_preferences():
    """Fetch all shift preferences from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shiftpreferences")
    shift_preferences = cursor.fetchall()
    conn.close()
    return shift_preferences

def fetch_all_seniority():
    """Fetch all seniority scores from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seniority")
    seniority = cursor.fetchall()
    conn.close()
    return seniority

def fetch_all_shift_requirements():
    """Fetch all shift requirements from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shiftrequirements")
    shift_requirements = cursor.fetchall()
    conn.close()
    return shift_requirements

print(fetch_all_shift_requirements())

#