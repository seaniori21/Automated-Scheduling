import { useState, useEffect } from "react";
import getToken from '../Components/useToken.jsx';
import {getTokens, useAuth} from '../Components/Auth.jsx';
import axios from "axios";
import UnavailableDays from "../Components/UnavailableDays.jsx";

const Test = () => {
    const [data, setData] = useState([]);

    const token = getToken()
    // const userUseAuth = useAu()

    
    useEffect(() => {
      fetch("http://127.0.0.1:5000/test", {
          'methods':'GET',
          headers: {
              'Authorization': `Bearer ${token.token}`
          }
      }).then(
          res => res.json()
      ).then(
          data => {
              setData(data)
              console.log(data)
          }
      ).catch(err => {
          console.log("Profile ERROR:",err)
      })
  }, [])
    


    
    ////
    const posts = [
      {id:1,  Day: 'Hello World', Job: 'Welcome to learning React!'},
      {id:2, Day: 'Installation', Job: 'You can install React from npm.'}
    ]
    console.log("Posts", posts)


    const shifts = data.Shifts
    console.log("Shifts", shifts)

    // Check if shifts is not null before mapping
    const content = shifts ? (
      shifts.map((post) => (
        <div key={post.id}>
          <p>{post.Day}: {post.Job}</p>
        </div>
      ))
    ) : (
      <p>Loading shifts...</p>
    );
    

    return ( 
        <div>

        <section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-dark text-white" >
          <div class="card-body p-5 text-center">

            <div class="pb-3">
            <h1 class="fw-bold mb-2 text-uppercase">Profile</h1>
            </div>

            <div class="mb-md-5 mt-md-4 pb-1">
                <h4 class="fw-bold mb-2 ">Employee ID Number: {data.ID}</h4> 
                <h4 class="fw-bold mb-2 text-uppercase">Name: {data.Name}</h4>
            </div>


            <div class="mb-md-1 mt-md-1 pb-1">
            <h4 class="fw-bold mb-2 text-uppercase">Shift Preferences</h4>
              {content}
            </div>

            <hr />

            <div class="mb-md-1 ">
                <UnavailableDays data={data} />
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</section>
    </div>
    );
}
 
export default Test;