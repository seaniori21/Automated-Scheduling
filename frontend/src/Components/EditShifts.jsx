import { useState, useEffect } from "react";
import axios from 'axios';
import getToken from '../Components/useToken.jsx';
import { useNavigate, useLocation } from 'react-router-dom';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

function EditShifts(props) {
  const navigate = useNavigate();
  const location = useLocation();
  const token = getToken()


  const [ID, setID] = useState('');
  const [ShiftJob, setJob] = useState('')
  const [ShiftDay, setDay] = useState('')
  const [Shifts, setShifts] = useState('')
  const [age, setAge] = useState('');

  const shiftNames = location.state.data
  console.log("ShiftNames",shiftNames)


  const [state, setState] = useState({
      Monday: '',
      Tuesday: '',
      Wednesday: '',
      Thursday: '',
      Friday: '',
      Saturday: '',
      Sunday: '',
  });

  const { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday } = state;
  
  const handleChange = (event) => {
    setState({
      ...state,
      [event.target.name]: event.target.value,
  });
  };

  const changeShifts = () => {
    if(0 != 0) {
        alert("Choose 2 options")
    }
    else{
        axios.post('http://127.0.0.1:5000/editShifts', {
        "Shifts": [1,2,3,4,5,6,7]
        }
        ,{
        headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token.token}`
        }
    })
        .then(function (response) {
        if (response.status === 200){
            alert("Success")  
            navigate("/test") 
        }
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
        <div class="card bg-whitetext-white" >
          <div class="card-body p-5 text-center">

            <div class=" pb-4">
            <h1 class="fw-bold text-uppercase">Edit</h1>
            </div>

            {/* Monday */}
            <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">
              
              <div className="col-md-6">
                <h4 class="fw-bold text-uppercase mt-md-2">Monday</h4>
              </div>
              <div className="col-md-6">
              <FormControl sx={{ m: 1, minWidth: 160 , backgroundColor: 'white'}} size="small">
                <InputLabel id="demo-select-small-label">Shifts</InputLabel>
                <Select
                  value={Monday}
                  name="Monday" 
                  onChange={handleChange}
                >
                  {shiftNames.map((option) => (
                    <MenuItem key={option} value={option}>
                      {option}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
              </div>
            </div>
            
            {/* Tuesday */}
            <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">
            <div className="col-md-6">
                <h4 class="fw-bold text-uppercase mt-md-2">Tuesday</h4>
              </div>
              <FormControl sx={{ m: 1, minWidth: 160 , backgroundColor: 'white'}} size="small">
                <InputLabel id="demo-select-small-label">Shifts</InputLabel>
                <Select
                  value={Tuesday}
                  name="Tuesday" 
                  onChange={handleChange}
                >
                  {shiftNames.map((option) => (
                    <MenuItem key={option} value={option}>
                      {option}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </div>
            
            {/* Wednesday */}
            <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">
            <div className="col-md-6">
                <h4 class="fw-bold text-uppercase mt-md-2">Wednesday</h4>
              </div>
              <FormControl sx={{ m: 1, minWidth: 160 , backgroundColor: 'white'}} size="small">
                <InputLabel id="demo-select-small-label">Shifts</InputLabel>
                <Select
                  value={Wednesday}
                  name="Wednesday" 
                  onChange={handleChange}
                >
                  {shiftNames.map((option) => (
                    <MenuItem key={option} value={option}>
                      {option}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </div>
                  
            {/* Thursday */}
            <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">
            <div className="col-md-6">
                <h4 class="fw-bold text-uppercase mt-md-2">Thursday</h4>
              </div>
              <FormControl sx={{ m: 1, minWidth: 160 , backgroundColor: 'white'}} size="small">
                <InputLabel id="demo-select-small-label">Shifts</InputLabel>
                <Select
                  value={Thursday}
                  name="Thursday" 
                  onChange={handleChange}
                >
                  {shiftNames.map((option) => (
                    <MenuItem key={option} value={option}>
                      {option}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </div>

            {/* Friday */}
            <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">
            <div className="col-md-6">
                <h4 class="fw-bold text-uppercase mt-md-2">Friday</h4>
              </div>
              <FormControl sx={{ m: 1, minWidth: 160 , backgroundColor: 'white'}} size="small">
                <InputLabel id="demo-select-small-label">Shifts</InputLabel>
                <Select
                  value={Friday}
                  name="Friday" 
                  onChange={handleChange}
                >
                  {shiftNames.map((option) => (
                    <MenuItem key={option} value={option}>
                      {option}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </div>

            {/* Saturday */}
            <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">
            <div className="col-md-6">
                <h4 class="fw-bold text-uppercase mt-md-2">Saturday</h4>
              </div>
              <FormControl sx={{ m: 1, minWidth: 160 , backgroundColor: 'white'}} size="small">
                <InputLabel id="demo-select-small-label">Shifts</InputLabel>
                <Select
                  value={Saturday}
                  name="Saturday" 
                  onChange={handleChange}
                >
                  {shiftNames.map((option) => (
                    <MenuItem key={option} value={option}>
                      {option}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </div>
            
            {/* Sunday*/}
            <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">
            <div className="col-md-6">
                <h4 class="fw-bold text-uppercase mt-md-2">Sunday</h4>
              </div>
              <FormControl sx={{ m: 1, minWidth: 160 , backgroundColor: 'white'}} size="small">
                <InputLabel id="demo-select-small-label">Shifts</InputLabel>
                <Select
                  value={Sunday}
                  name="Sunday" 
                  onChange={handleChange}
                >
                  {shiftNames.map((option) => (
                    <MenuItem key={option} value={option}>
                      {option}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </div>


          </div>

          <button class="btn btn-outline-light btn-lg px-5" onClick={changeShifts} >Update</button>
          <div>
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