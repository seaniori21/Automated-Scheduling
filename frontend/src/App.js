import './App.css';

import Home from './Pages/Home';
import Login from './Components/Login';
import EmployeeSignUp from './Components/EmployeeSignUp';
import Test from "./Pages/Profile.jsx";
import NavBar from './Components/NavBar';
import Header from './Components/Header';

import {Routes, Route} from  "react-router-dom";
import useToken from './Components/useToken'
import {useAuth} from './Components/Auth'
import EditShifts from './Components/EditShifts.jsx';
import EditOffDays from './Components/EditOffDays.jsx';


function App() {
  const { setToken } = useToken();
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
              <Route path="/EditShifts" element={<EditShifts/>} />
              <Route path="/editdaysoff" element={<EditOffDays/>} />
          </>
      )}
      
      </Routes>
      <footer class="py-5 bg-dark">
      <div class="footer"><p class="m-0 text-center text-white">Copyright &copy; Auto Scheduling 2023</p></div>
    </footer>
      
      
      
    </div>
  )
}

export default App;
