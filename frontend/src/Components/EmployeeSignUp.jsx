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
      <form onSubmit={handleSubmit}>
        {/* Input fields for first name, last name, email, password */}
        {/* ... */}
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
}

export default EmployeeSignUp;
