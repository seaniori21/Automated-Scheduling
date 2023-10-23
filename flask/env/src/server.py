from flask import Flask, jsonify, request, session
from flask_bcrypt import Bcrypt 
from flask_cors import CORS
from models import db, User, Employer

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
    app.run(debug=True)