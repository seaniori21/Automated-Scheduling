import React, {useState, useEffect} from 'react';
import './App.css';

import Home from './Pages/Home';
import EmployerSignUp from './Components/EmployerSignUp.jsx';
import Login from './Components/Login';
import EmployeeConfirmation from './Components/EmployeeCheck';
import EmployeeSignUp from './Components/EmployeeSignUp';
import Test from "./Pages/test";
import NavBar from './Components/NavBar';
import Header from './Components/Header';
import ProtectedRoute from './Components/ProtectedRoute.jsx';

import {Routes, Route} from  "react-router-dom";
import useToken from './Components/useToken'
import {useAuth} from './Components/Auth'
import Profile from './Components/Profile';


function App() {
  const { token, removeToken, setToken } = useToken();
  const [logged] = useAuth(); 
  return (
    <div className="App">
      
      <NavBar/>
      <Routes>
      {!logged && (
                    <>
                        <Route path="/Header" element={<Header/>} />
                        <Route path="/" element={<Header/>} />
                        <Route path="/login" element={<Login setToken={setToken}/>} />
                        <Route path="/EmployeeSignUp" element={<EmployeeSignUp/>} />
                    </>
                )}
      {logged && (
          <>
              <Route path="/Home" element={<Home/>} exact />
              <Route path="/" element={<Home/>} exact />
              <Route path="/test" element={<Test/>} exact />
          </>
      )}

        {/* <Route path="/" element={<Header/>}/>
        <Route path="/Home" element={<ProtectedRoute> <Home /> </ProtectedRoute>} />
        <Route path="/Header" element={<Header/>}/>
        <Route path="/Login" element={<Login/>}/>
        <Route path="/EmployerSignUp" element={<EmployerSignUp/>}/>
        <Route path="/EmployeeConfirmation" element={<EmployeeConfirmation/>}/>
        <Route path="/EmployeeSignUp" element={<EmployeeSignUp/>}/>
        <Route path="/test" element={<Test/>}/> */}
      
      </Routes>
      
      
      
    </div>
  )
}

export default App;