import { useState, useEffect } from "react";
import getToken from '../Components/useToken.jsx';
import {getTokens, useAuth} from '../Components/Auth.jsx';
import axios from "axios";
import UnavailableDays from "../Components/UnavailableDays.jsx";
import EditOffDays from "../Components/EditOffDays.jsx";
import { useNavigate, Navigate } from 'react-router-dom';

const Test = () => {
    const [data, setData] = useState([]);
    const [isButtonClicked, setIsButtonClicked] = useState(false);
    const navigate = useNavigate()

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

    const shifts = data.Shifts
    // Check if shifts is not null before mapping
    const content = shifts ? (
      shifts.map((shift) => (
        <div key={shift.id}>
          <p>{shift.Day}: {shift.Job}</p>
        </div>
      ))
    ) : (
      <p>Loading shifts...</p>
    );

    const DisplayEditOffDays = () => {
      // Set the state to true when the button is clicked

      setIsButtonClicked(true);
      navigate("/editdaysoff")
    };

    const editShifts = () => {
      axios({
        method: "GET",
        url:"/getShiftNames",
        headers: {
          Authorization: 'Bearer ' + token.token
        }
      })
      .then((response) => {
        const data = response.data.Shifts
        navigate('/EditShifts', { state:{data} });
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      })
    }

    const displayEditShifts = () => {
        editShifts()
      
    };
    

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

            <div>
                  <button class="btn btn-outline-light btn-xs px-5" onClick={displayEditShifts}>Get Shift Names</button>
            </div>

            <hr />

            <div class="mb-md-1 ">
                <UnavailableDays data={data} />

                <div>
                  <button class="btn btn-outline-light btn-xs px-5" onClick={DisplayEditOffDays}>Change Your Availability</button>
                </div>
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