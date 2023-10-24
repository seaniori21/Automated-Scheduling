import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

function EmployeeCheck() {
  const [companyName, setCompanyName] = useState('');
  const [employerEmail, setEmployerEmail] = useState('');
  const [employeeEmail, setEmployeeEmail] = useState('');

  const navigate = useNavigate(); // Initialize useNavigate

  const handleConfirmation = () => {
    axios.post('http://127.0.0.1:5000/EmployeeConfirmation', {
      companyName,
      employerEmail,
      employeeEmail,
    })
    .then((response) => {
      if (response.status === 200) {
        console.log('Confirmation successful');
        // Redirect the user to the EmployeeSignUpPage
        navigate('/EmployeeSignUpPage');
      } else {
        console.error('Confirmation failed:', response.data.error);
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  };

  return (
    <div>
      <section className="vh-100 gradient-custom">
        <div className="container py-5 h-100">
          <div className="row d-flex justify-content-center align-items-center h-100">
            <div className="col-12 col-md-8 col-lg-6 col-xl-5">
              <div className="card bg-dark text-white">
                <div className="card-body p-5 text-center">

                  <div className="mb-md-5 mt-md-4 pb-5">
                    <h2 className="fw-bold mb-2 text-uppercase">Confirmation</h2>
                    <p className="text-white-50 mb-5">Please Make your login and password!</p>

                    <div className="form-outline form-white mb-4">
                      <input
                        type="text"
                        value={companyName}
                        onChange={(e) => setCompanyName(e.target.value)}
                        id="typeCompanyX"
                        className="form-control form-control-lg"
                      />
                      <label className="form-label" htmlFor="typeCompanyX">Company Name</label>
                    </div>

                    <div className="form-outline form-white mb-4">
                      <input
                        type="email"
                        value={employerEmail}
                        onChange={(e) => setEmployerEmail(e.target.value)}
                        id="typeEmployerEmailX"
                        className="form-control form-control-lg"
                      />
                      <label className="form-label" htmlFor="typeEmployerEmailX">Employer Email</label>
                    </div>

                    <div className="form-outline form-white mb-4">
                      <input
                        type="email"
                        value={employeeEmail}
                        onChange={(e) => setEmployeeEmail(e.target.value)}
                        id="typeEmployeeEmailX"
                        className="form-control form-control-lg"
                      />
                      <label className="form-label" htmlFor="typeEmployeeEmailX">Your Email</label>
                    </div>

                    <button
                      className="btn btn-primary btn-lg px-4 me-sm-3"
                      onClick={handleConfirmation}
                    >
                      Confirm
                    </button>
                  </div>

                  <div>
                    <p className="mb-0">Already have an account? <a href="/LoginPage" className="text-white-50 fw-bold"> Click here to login</a></p>
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

export default EmployeeCheck;
