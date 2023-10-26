from flask import Flask, jsonify, request, session

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from models import db, User, Employer, Employee

app = Flask(__name__)

app.config['SECRET_KEY'] = 'group6-senior-design'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

SQLALCHEMY_TRACK_MODIFICATION = False
SQLALCHEMY_ECHO = True

bcrypt = Bcrypt(app) 
CORS(app,supports_credentials=True)#To pass CORS policy
db.init_app(app)

with app.app_context():
    db.create_all()

#Members for API Route/Pages
@app.route('/')
def homepage():
    return "Hello World"


@app.route('/EmployerSignUp', methods=['POST'])
def signup():

    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    password = request.json["password"]
    company = request.json["company"]


    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"Error" : "Email already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password)
    new_user = Employer(email=email, password=hashed_password, firstname=firstname, lastname=lastname, company=company)
    db.session.add(User(email=new_user.email, password=hashed_password, id=new_user.id))
    db.session.add(new_user)

    db.session.commit()

    session['user_id'] = new_user.id

    response_body = jsonify({
        "id:": new_user.id,
        "email:": new_user.email,
        "Name:" : new_user.firstname + " " + new_user.lastname,
        "Company:" : new_user.company
    })  

    return response_body

from flask_cors import cross_origin

@app.route('/EmployeeConfirmation', methods=['POST'])
@cross_origin()  # Enable CORS for this route
def employee_confirmation():
    # Get the data from the POST request
    company_name = request.json["companyName"]
    employer_email = request.json["employerEmail"]

    # Check if the employer email exists in the Employer table
    employer = Employer.query.filter_by(email=employer_email).first()

    if employer is None:
        # If the employer email doesn't exist, return an error response
        return jsonify({"error": "Employer email not found"}), 400

    # If the employer email exists,  returning a success response (temporary)
    return jsonify({"message": f"Company: {company_name}, Employer: {employer.email} confirmed"}), 200


@app.route('/EmployeeSignUp', methods=['POST'])
def employee_signup():
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    password = request.json["password"]

    # Check if the user already exists
    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"Error": "Email already exists"}), 409

    # Hash the password and create a new Employee instance
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = Employee(email=email, password=hashed_password, firstname=firstname, lastname=lastname)

    # Add to both User and Employee tables
    db.session.add(User(email=new_user.email, password=hashed_password, id=new_user.id))
    db.session.add(new_user)
    db.session.commit()

    session['user_id'] = new_user.id

    response_body = jsonify({
        "id": new_user.id,
        "email": new_user.email,
        "Name": new_user.firstname + " " + new_user.lastname,

        # Include other employee-specific data in the response
    })

    return response_body


@app.route('/login', methods=['POST'])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"Error" : "Email does not exist"}), 401
    
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"Error" : "Wrong Password"}), 401
    
    session["user_id"] = user.id

    response_body = jsonify({
        "id:": user.id,
        "email:": user.email,
    })  

    return response_body

if __name__ == '__main__':
    print(app)
    app.run(debug=True)