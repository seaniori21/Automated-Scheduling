import React from 'react'

function UnavailableDays(daysOff) {
  return (
    <div>
      <h4 class="Profile">Unavailable Days</h4>
      <p class="fw-bold mb-2 ">
          {daysOff.data.UnavailableDays}
      </p>
    </div>
  )
}

export default UnavailableDays