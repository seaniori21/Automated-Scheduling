import React, {useState, useEffect} from 'react';
import './App.css';

import HomePage from './Pages/HomePage';
import EmployerSignUp from './Pages/EmployerSignUp';
import LoginPage from './Pages/LoginPage';
import EmployeeConfirmation from './Pages/EmployeeConfirmation';
import EmployeeSignUpPage from './Pages/EmployeeSignUpPage';


import {BrowserRouter, Routes, Route} from  "react-router-dom";


function App() {

  

  return (
    <div>

      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/Homepage" element={<HomePage/>}/>
        <Route path="/LoginPage" element={<LoginPage/>}/>
        <Route path="/EmployerSignUp" element={<EmployerSignUp/>}/>
        <Route path="/EmployeeConfirmation" element={<EmployeeConfirmation/>}/>
        <Route path="/EmployeeSignUpPage" element={<EmployeeSignUpPage/>}/>

      </Routes>      
      
      
    </div>
  )
}

export default App;
