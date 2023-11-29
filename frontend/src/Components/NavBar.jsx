import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
import axios from 'axios'
import useToken from './useToken';
import { useAuth ,logout} from './Auth'


function NavBar(props) {

  const navigate = useNavigate();

  function logMeOut() {
    axios({
      method: "POST",
      url:"/logout",
    })
    .then((response) => {
      navigate("/Header")
      console.log("YOLOOOOOOO")
      console.log(response); 
      logout();
      props.token()
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

    const LoggedInLinks = () => {
      return (
          <>
              <li className="nav-item">
                  <a className="nav-link active" href="#" onClick={()=>{logMeOut()}}>Log Out</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/Home">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/test">Profile</a>
              </li>
          </>
      )
  }
  
  
  const LoggedOutLinks = () => {
      return (
          <>
          <li class="nav-item"><a class="nav-link active" aria-current="page" href="/Login">Login</a></li>
          <li class="nav-item"><a class="nav-link active" aria-current="page" href="/Header">Header</a></li>
          </>
      )
  }
     const [logged] = useAuth();

  return (
    <div>
        <div>

       <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container px-5">
            <a class="navbar-brand" href="#!">Auto Scheduling</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                   {logged?<LoggedInLinks/>:<LoggedOutLinks/>}
                    {/* <li class="nav-item"><a class="nav-link active" aria-current="page" href="/HomePage">Home</a></li> */}
                </ul>
            </div>
        </div>
    </nav>
  </div>
    </div>
  )
}

export default NavBar