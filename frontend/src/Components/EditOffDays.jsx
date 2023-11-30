import * as React from 'react';
import Box from '@mui/material/Box';
import FormLabel from '@mui/material/FormLabel';
import FormControl from '@mui/material/FormControl';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormHelperText from '@mui/material/FormHelperText';
import Checkbox from '@mui/material/Checkbox';
import axios from 'axios'
import { useNavigate } from 'react-router-dom';
import getToken from '../Components/useToken.jsx';


function EditOffDays() {

    const navigate = useNavigate();
    const token = getToken()

    const [state, setState] = React.useState({
        Monday: false,
        Tuesday: false,
        Wednesday: false,
        Thursday: false,
        Friday: false,
        Saturday: false,
        Sunday: false,
    });
    
    const handleChange = (event) => {
    setState({
        ...state,
        [event.target.name]: event.target.checked,
    });
    };
    
    const { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday } = state;
    const error = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday].filter((v) => v).length !== 2;
    const trueDaysArray = Object.keys(state)
        .filter((day) => state[day])
        .map((day) => {
            switch (day) {
            case 'Monday':
                return 0;
            case 'Tuesday':
                return 1;
            case 'Wednesday':
                return 2;
            case 'Thursday':
                return 3;
            case 'Friday':
                return 4;
            case 'Saturday':
                return 5;
            case 'Sunday':
                return 6;
            default:
                return -1; // Handle unknown days
            }
    });

    const changeOffDays = () => {
    if(error) {
        alert("Choose 2 options")
    }
    else{
        axios.post('http://127.0.0.1:5000/editDaysOff', {
        "UnavailableDays": trueDaysArray
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
    <section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-dark text-white" >
          <div class="card-body p-5 text-center">

    <div>

      
      <FormControl
        required
        error={error}
        component="fieldset"
        sx={{ m: 3 }}
        variant="standard"
      >
        <FormLabel component="legend">Pick two</FormLabel>
        <FormGroup>
          <FormControlLabel
            control={
              <Checkbox checked={Monday} onChange={handleChange} name="Monday" />
            }
            label="Monday"
          />
          <FormControlLabel
            control={
              <Checkbox checked={Tuesday} onChange={handleChange} name="Tuesday" />
            }
            label="Tuesday"
          />
          <FormControlLabel
            control={
              <Checkbox checked={Wednesday} onChange={handleChange} name="Wednesday" />
            }
            label="Wednesday"
          />
          <FormControlLabel
            control={
              <Checkbox checked={Thursday} onChange={handleChange} name="Thursday" />
            }
            label="Thursday"
          />
          <FormControlLabel
            control={
              <Checkbox checked={Friday} onChange={handleChange} name="Friday" />
            }
            label="Friday"
          />
          <FormControlLabel
            control={
              <Checkbox checked={Saturday} onChange={handleChange} name="Saturday" />
            }
            label="Saturday"
          />
          <FormControlLabel
            control={
              <Checkbox checked={Sunday} onChange={handleChange} name="Sunday" />
            }
            label="Sunday"
          />
        </FormGroup>
        <FormHelperText>You can only pick 2</FormHelperText>
      </FormControl>
    </div>

    <button class="btn btn-outline-light btn-lg px-5" onClick={changeOffDays} >Update</button>
        </div>
      </div>
    </div>
  </div>
  </div>
</section>

  )
}

export default EditOffDays