import React from 'react'

//Used for the homepage setup
function Header() {
  return (
    <div>
        <section class="vh-100 gradient-custom">
    <header className="bg-dark py-5">
        <div className="container px-5">
            <div className="row gx-5 justify-content-center">
                <div className="col-lg-6">
                    <div className="text-center my-5">
                        <h1 className="display-5 fw-bolder text-white mb-2">Are you having trouble making schedules?</h1>
                        <p className="lead text-white-50 mb-4">Quickly design and customize your schedules for your company today!</p>
                        <div className="d-grid gap-3 d-sm-flex justify-content-sm-center">
                            <a className="btn btn-primary btn-lg px-4 me-sm-3" href="/EmployerSignUp">Employer</a>
                            <a className="btn btn-outline-light btn-lg px-4" href="/EmployeeConfirmation">Employee</a>
                        </div>

                    </div>
                    <div className="text-center my-5">
                    <a className="lead text-white-50 mb-4 " href="\LoginPage">If you already have an account. Click here!!!</a>
                    </div>
                    
                </div>
            </div>
        </div>
    </header>
    </section>
    </div>
  )
}

export default Header