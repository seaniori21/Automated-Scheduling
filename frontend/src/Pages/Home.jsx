import React from 'react'
import Schedule from '../Components/Schedule.jsx';

function Home() {

  return (
    <div>
        <section class="vh-100 gradient-custom">
    <header>
        <h1>Weekly Schedule</h1>
        <div className="container px-5">
            <div className="row gx-5 justify-content-center">
                <div className="col-lg-6">
                    <div className="text-center my-5">
                        <div ><Schedule/></div>
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