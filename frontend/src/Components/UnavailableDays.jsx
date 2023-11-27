import React from 'react'

function UnavailableDays(daysOff) {
    console.log("HERE", daysOff)
  return (
    <p class="fw-bold mb-2 text-uppercase">
        Unavailable Days: {daysOff.data.UnavailableDays}
    </p>
  )
}

export default UnavailableDays