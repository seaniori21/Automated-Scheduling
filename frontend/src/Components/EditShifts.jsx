import { useState, useEffect } from "react";
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import getToken from './useToken.jsx';
import {useAuth} from './Auth.jsx';
import UnavailableDays from "./UnavailableDays.jsx";

function EditShifts() {
    const navigate = useNavigate();

  const [ID, setID] = useState('');
  const [ShiftJob, setJob] = useState('')
  const [ShiftDay, setDay] = useState('')
  const [Shifts, setShifts] = useState('')


  const editShifts = () => {
    if(ShiftDay.length === 0) {
      alert("Day has been left blank")
    }
    if(ShiftJob.length === 0) {
      alert("Job has been left blank")
    }
    else{
      axios.post('http://127.0.0.1:5000/editShifts', {
        ID: ID,
        ShiftDay: ShiftDay,
        ShiftJob: ShiftJob
      })
      .then(function (response) {
        
        // navigate("/login")
         
      })
      .catch(function (error) {
        console.log(error, 'error');
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
        }
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

            <div class="mb-md-1 mt-md-4 pb-1">
            <h1 class="fw-bold mb-2 text-uppercase">Edit</h1>
            </div>

            <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">

                <div className="form-outline form-white mb-4">
                  <input type="lastname" value={ShiftJob} onChange={(e) => setJob(e.target.value)} id="typeLastName" className="form-control form-control-lg" />
                  <label className="form-label" htmlFor="typeLastName">Last Name</label>
                </div>

                <div className="form-outline form-white mb-4">
                  <input type="lastname" value={ShiftJob} onChange={(e) => setJob(e.target.value)} id="typeLastName" className="form-control form-control-lg" />
                  <label className="form-label" htmlFor="typeLastName">Last Name</label>
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

export default EditShifts