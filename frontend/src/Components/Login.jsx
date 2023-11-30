import React, {useState} from 'react'
import axios from 'axios'
import setToken from './useToken'
import { useNavigate } from 'react-router-dom';
import {login} from './Auth'

function Login(props) {

  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('')

  

  const logInUser = () => {
    if(email.length === 0) {
      alert("Email has been left blank")
    }
    if(password.length === 0) {
      alert("Password has been left blank")
    }
    else{
      axios.post('http://127.0.0.1:5000/token', {
        email: email,
        password: password
      })
      .then(function (response) {
        
        if (response.status === 200){
          console.log(response.data.access_token);
          login(response.data.access_token)
          props.setToken(response.data.access_token)
          navigate("/Home")
          
        }
      })
      .catch(function (error) {
        console.log(error, 'error');
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
        }
        alert("Wrong Authentication")
      });
    }
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

              <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
              <p class="text-white-50 mb-5">Please enter your login and password!</p>

              <div class="form-outline form-white mb-4">
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} id="typeEmailX" class="form-control form-control-lg" />
                <label class="form-label" for="typeEmailX">Email</label>
              </div>

              <div class="form-outline form-white mb-4">
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} id="typePasswordX" class="form-control form-control-lg" />
                <label class="form-label" for="typePasswordX">Password</label>
              </div>
              

              <p class="small mb-5 pb-lg-2"><a class="text-white-50" href="#!">Forgot password?</a></p>

              <button class="btn btn-outline-light btn-lg px-5" onClick={logInUser} >Login</button>

              <div class="d-flex justify-content-center text-center mt-4 pt-1">
                <a href="#!" class="text-white"><i class="fab fa-facebook-f fa-lg"></i></a>
                <a href="#!" class="text-white"><i class="fab fa-twitter fa-lg mx-4 px-2"></i></a>
                <a href="#!" class="text-white"><i class="fab fa-google fa-lg"></i></a>
              </div>

            </div>

            <div>
              <p class="mb-0">Don't have an account? <a href="\EmployerSignUp" class="text-white-50 fw-bold">Sign Up</a>
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

export default Login