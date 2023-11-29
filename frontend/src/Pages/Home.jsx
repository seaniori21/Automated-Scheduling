import React from 'react'
//import Header from 'C:/Users/seani/OneDrive/Documents/FALL 2023/Senior Design/Automated Scheduling/frontend/src/Components/NavBar.jsx';
import Header from '../Components/Header.jsx';
import Schedule from '../Components/Schedule.jsx';

function Home() {
  return (
    <div>
        <section class="vh-100 gradient-custom">
    <header className="bg-dark py-5">
        <div className="container px-5">
            <div className="row gx-5 justify-content-center">
                <div className="col-lg-6">
                    <div className="text-center my-5">
                        <div><Schedule/></div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    </section>
    </div>
  )
}

export default Home