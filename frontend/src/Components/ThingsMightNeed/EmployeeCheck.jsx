import React from 'react'

function EmployeeCheck() {
  return (
    <div>     <section class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card bg-dark text-white" >
            <div class="card-body p-5 text-center">
  
              <div class="mb-md-5 mt-md-4 pb-5">
  
  
                <h2 class="fw-bold mb-2 text-uppercase">Confirmation</h2>
                <p class="text-white-50 mb-5">Please Make your login and password!</p>
  

  
                <div class="form-outline form-white mb-4">
                  <input type="company" id="typeCompanyX" class="form-control form-control-lg" />
                  <label class="form-label" for="typeCompanyX">Company Name</label>
                </div>

                <div class="form-outline form-white mb-4">
                  <input type="email" id="typeEmployerEmailX" class="form-control form-control-lg" />
                  <label class="form-label" for="typeEmailX">Employer Email</label>
                </div>
  
                <div class="form-outline form-white mb-4">
                  <input type="email" id="typeEmployeeEmailX" class="form-control form-control-lg" />
                  <label class="form-label" for="typeEmailX">Your Email</label>
                </div>
                
  
                {/* <button class="btn btn-outline-light btn-lg px-5" type="submit" href="/EmployeeSignUpPage">Confirm</button> */}
                <a className="btn btn-primary btn-lg px-4 me-sm-3" href="/EmployeeSignUpPage">Confirm</a>

  
              </div>
  
              <div>
                <p class="mb-0">Already have an account? <a href="\LoginPage" class="text-white-50 fw-bold"> Click here to login</a>
                </p>
              </div>
  
            </div>
          </div>
        </div>
      </div>
    </div>
  </section></div>
  )
}

export default EmployeeCheck