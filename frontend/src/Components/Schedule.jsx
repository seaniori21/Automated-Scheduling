import { useState, useEffect } from "react";
import axios from "axios";
import React from "react";


function Schedule(props) {
  const [sched, setSched] = useState([]);

  useEffect(() => {
    axios({
      method: "GET",
      url: "/Schedule",
      headers: {
        Authorization: "Bearer " + props.token,
      },
    })
      .then((response) => {
        setSched(response.data);
        console.log(sched[0].shifts);
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  }, []);
  console.log(sched[0]);
  const schedName = sched[0]?.shifts;
  console.log(schedName);

  // function getData() {
  //   axios({
  //     method: "GET",
  //     url:"/Schedule",
  //     headers: {
  //       Authorization: 'Bearer ' + props.token
  //     }
  //   })
  //   .then((response) => {
  //     setSched(response.data)
  //     console.log(sched[0].shifts)

  //   }).catch((error) => {
  //     if (error.response) {
  //       console.log(error.response)
  //       console.log(error.response.status)
  //       console.log(error.response.headers)
  //       }
  //   }, [])}

  // const content = sched[0].shifts ? (
  //     sched[0].shifts.map((shift)=>
  //     (
  //         <div>
  //             <th key= {shift.shift_name} > {shift.shift_name} </th>

  //         </div>

  //     ))
  // ): (
  //     <p> Loading Shifts...</p>
  // );

  const daysOfWeek = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ];

  return (
    <div className="Scheduler">
      <table className="schedule">
        <thead className="schedHead">
          <tr className="trSchedHead">
            <th className="th"> Day/Shift</th>
            {schedName?.map((shift) => (
              <th className="th" key={shift.shift_name}>{shift.shift_name}</th>
            ))}
          </tr>
        </thead>
        <tbody className="schedBody">
          {sched.map((dayInfo, index) => (
            <tr className="trSchedBody" key={index}>
              <td className="tdSchedDays">{daysOfWeek[dayInfo.day]}</td>
              {dayInfo.shifts.map((shiftInfo, shiftIndex) => (
                <td className="tdSchedNames" key={shiftIndex}>{shiftInfo.employees.join(", ")}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Schedule;
