import React from 'react'

import { useState } from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function EmployerSignUp() {

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('')
  const [firstname, setFirstName] = useState('')
  const [lastname, setLastName] = useState('')
  const [company, setCompany] = useState('')

  const navigate = useNavigate();
  const registerUser = () => {
    axios.post('http://127.0.0.1:5000/EmployerSignUp', {
        firstname: firstname,
        lastname: lastname,
        company: company,
        email: email,
        password: password
      })
      .then(function (response) {
        console.log(response);
        navigate("/LoginPage")

        // if (response.status === 200){
        //   alert("Success")
        // }
        //console.log(response.data)
      })
      .catch(function (error) {
        console.log(error, 'error');
        if (error.response.status === 500){
          alert("Email already exists")
        }
    });    
  }
  


  return (
    <div>
         <section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-dark text-white" >
          <div class="card-body p-5 text-center">

            <div class="mb-md-5 mt-md-4 pb-5">


              <h2 class="fw-bold mb-2 text-uppercase">SignUp</h2>
              <p class="text-white-50 mb-5">Please Make your login and password!</p>

              <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">
                    <div class="form-outline form-white mb-4">
                      <input type="firstname" value={firstname} onChange={(e) => setFirstName(e.target.value)} id="typeFirstNameX" class="form-control form-control-lg" />
                      <label class="form-label" for="typeFirstName">First Name</label>
                    </div>
                    <div class="form-outline form-white mb-4">
                      <input type="lastname" value={lastname} onChange={(e) => setLastName(e.target.value)} id="typeLastName" class="form-control form-control-lg" />
                      <label class="form-label" for="typeLastName">Last Name</label>
                    </div>
              </div>

              

              <div class="form-outline form-white mb-4">
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} id="typeEmailX" class="form-control form-control-lg" />
                <label class="form-label" for="typeEmailX">Email</label>
              </div>

              <div class="form-outline form-white mb-4">
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} id="typePasswordX" class="form-control form-control-lg" />
                <label class="form-label" for="typePasswordX">Password</label>
              </div>
              
              <div class="form-outline form-white mb-4">
                <input type="company" value={company} onChange={(e) => setCompany(e.target.value)} id="typeCompanyX" class="form-control form-control-lg" />
                <label class="form-label" for="typeCompanyX">Company Name</label>
              </div>

              <button class="btn btn-outline-light btn-lg px-5" onClick={() => registerUser()} >Sign Up</button>

              {/* <div class="d-flex justify-content-center text-center mt-4 pt-1">
                <a href="#!" class="text-white"><i class="fab fa-facebook-f fa-lg"></i></a>
                <a href="#!" class="text-white"><i class="fab fa-twitter fa-lg mx-4 px-2"></i></a>
                <a href="#!" class="text-white"><i class="fab fa-google fa-lg"></i></a>
              </div> */}

            </div>

            <div>
              <p class="mb-0">Already have an account? <a href="\LoginPage" class="text-white-50 fw-bold"> Click here to login</a>
              </p>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</section>

    </div>
  )
}

export default EmployerSignUp