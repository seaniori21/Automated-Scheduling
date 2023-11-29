import os
from flask import Flask, json, jsonify, make_response, render_template, request
from blueprints.employees_blueprint import employees
from blueprints.shifts_blueprint import shifts
from blueprints.requirements_blueprint import requirements
from blueprints.output_blueprint import output
from flask_cors import CORS
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager
import sqlite3

from database.insert_data import SchedulingDB

app = Flask(__name__)
CORS(app)


def get_db_connection():
    BASE_DIR = os.path.dirname(os.path.abspath("scheduling.db"))
    db_path = os.path.join(BASE_DIR, "scheduling.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


# app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)


@app.route('/editDaysOff', methods=["POST"])
@jwt_required()
def editDaysOff():
    ID = get_jwt_identity() # Filter DB by token (email)
    # ID = request.json.get("ID", None)
    offDays = request.json.get("UnavailableDays", None)

    print(ID)

    db = SchedulingDB('scheduling.db')
    db.delete_unavailable_days(ID)
    db.insert_unavailable_days(ID,offDays)
    db.close()

    return {"MSG":"Your Unavailable Days Have Been Updated"},200


@app.route('/editShifts', methods=["POST"])
@jwt_required()
def editShifts():
    ID = get_jwt_identity() # Filter DB by token (email)
    Shifts = request.json.get("Shifts", None)

    for Day,Job in Shifts.items():
        conn = get_db_connection()

        cur = conn.cursor()
        cur.execute("Select * FROM ShiftPreferences WHERE employee_id = ? AND day = ?", (ID, Day))
        existDay = cur.fetchone()
        
        #find if shiftday exists and if it does, delete it and put whatever he wants in
        if existDay:
            cur.execute("DELETE FROM ShiftPreferences WHERE employee_id = ? AND day = ?", (ID, Day))
            conn.commit()
        else:
            cur.execute("INSERT INTO ShiftPreferences (employee_id, day, preference) VALUES (?, ?, ?)", (ID, Day, Job))
            conn.commit()
        
    conn.close()

        
    return {"msg": "Shifts Successfully Updated"}


# routes
@app.route('/test', methods=['GET'])
@jwt_required()
def test():

    day_mapping = {1: 'Sunday ', 2: 'Monday ', 3: 'Tuesday ', 
                   4: 'Wednesday ', 5: 'Thursday ', 6: 'Friday ', 7: 'Saturday ',
    }

    id = get_jwt_identity() # Filter DB by token (email)


    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM Shifts")
    ShiftsNames = cur.fetchall()
    ShiftsNames_map = {id: name for id, name in ShiftsNames}  

    cur.execute("SELECT * FROM Employees WHERE id = ?", (id,))
    userId = cur.fetchone()

    cur.execute("SELECT * FROM ShiftPreferences WHERE employee_id = ?", (id,))
    userShiftPreferences = cur.fetchall()
    
    shiftsList= []
    if userShiftPreferences is not None:
        for column in userShiftPreferences:
            id_val, day, job = column
            Shifts = {}
            Shifts["Day"] = day_mapping[day]
            Shifts["Job"] = ShiftsNames_map[job]
            shiftsList.append(Shifts)

    else:
        Shifts["None"] = "None"
        shiftsList.append(Shifts)


    cur.execute("SELECT * FROM UnavailableDays WHERE employee_id = ?", (id,))
    userUnavailableDays = cur.fetchall()
    UnavailableDays = []
    if userUnavailableDays is not None:
        for column in userUnavailableDays:
            id_val, day = column
            UnavailableDays.append(day)
    else:
        UnavailableDays.append("None")

    # Mapping of numbers to days
    offDays = [day_mapping[number] for number in UnavailableDays]
    
    conn.close()

    return jsonify({
        'ID': userId[0],
        'Name': userId[1],
        'Shifts': shiftsList,
        "UnavailableDays": offDays
    })

@app.route('/token', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    conn = get_db_connection()

    cur = conn.cursor()
    cur.execute("SELECT * FROM Employees WHERE name = ?", (email,))
    user = cur.fetchone()
    conn.close()

    print(user[1],user[2])
    if email != user[1] or password != user[2]:
        return {"msg": "Wrong email or password"}, 401

    access_token = create_access_token(identity=user[0])
    response = {"access_token":access_token}
    return response

@app.route('/refresh', methods=["POST", "GET"])
def post():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return make_response(jsonify({"access_token": new_access_token}), 200)


@app.route('/signup', methods=["POST"])
def create_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    conn = get_db_connection()

    cur = conn.cursor()
    cur.execute("SELECT * FROM Employees WHERE name = ?", (email,))
    user = cur.fetchone()
    conn.close()

    if user:
        return {"msg": "Email Already Exists"}, 401

    db = SchedulingDB('scheduling.db')
    db.new_employee(email,password)
    db.close()
    
    return make_response(jsonify({"message": "User created successfuly"}), 201)


@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response





#Below Code is no relation to front end

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # This should be a random byte string.

app.register_blueprint(employees, url_prefix='/employees')
app.register_blueprint(shifts, url_prefix='/shifts')
app.register_blueprint(requirements, url_prefix='/requirements')
app.register_blueprint(output, url_prefix='/output')

@app.route('/')
def view():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(threaded=False)
