import React, { useState } from 'react';

function EmployeeSignUp() {
  // Define state variables to store user input
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent the default form submission behavior

    // Form validation logic (you can add more checks)
    if (!firstName || !lastName || !email || !password) {
      console.error('All fields are required.');
      return;
    }

    // Create an object with user data
    const userData = {
      firstName,
      lastName,
      email,
      password,
    };

    // Send the userData to the backend using a POST request
    fetch('http://127.0.0.1:5000/EmployeeSignUp', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the backend
        if (data.success) {
          // Registration was successful
          // You can optionally redirect the user to a confirmation page
          // Or display a confirmation message on the signup page
          console.log('Registration successful');
        } else {
          // Registration failed, handle the error
          console.error('Registration failed:', data.error);
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
                  {/* Form element */}
                  <form onSubmit={handleSubmit}>
                    <h2 className="fw-bold mb-2 text-uppercase">SignUp</h2>
                    <p className="text-white-50 mb-5">Employee Please Make your login and password!</p>

                    {/* First Name */}
                    <div className="form-outline form-white mb-4">
                      <input
                        type="text"
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                        id="typeFirstNameX"
                        className="form-control form-control-lg"
                        placeholder="First Name"
                      />
                    </div>

                    {/* Last Name */}
                    <div className="form-outline form-white mb-4">
                      <input
                        type="text"
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                        id="typeLastName"
                        className="form-control form-control-lg"
                        placeholder="Last Name"
                      />
                    </div>

                    {/* Email */}
                    <div className="form-outline form-white mb-4">
                      <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        id="typeEmailX"
                        className="form-control form-control-lg"
                        placeholder="Email"
                      />
                    </div>

                    {/* Password */}
                    <div className="form-outline form-white mb-4">
                      <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        id="typePasswordX"
                        className="form-control form-control-lg"
                        placeholder="Password"
                      />
                    </div>

                    <button className="btn btn-outline-light btn-lg px-5" type="submit">
                      Sign Up
                    </button>
                  </form>

                  <div>
                    <p className="mb-0">Already have an account? <a href="\LoginPage" className="text-white-50 fw-bold"> Click here to login</a></p>
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

export default EmployeeSignUp;
