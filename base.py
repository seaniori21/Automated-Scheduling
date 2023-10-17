from ortools.sat.python import cp_model
import matplotlib.pyplot as plt
import numpy as np


class Scheduler:
    def __init__(self, employee_data=None, shift_data=None, preferences=None, seniority=None, shift_requirements=None):

        self.employee_names = employee_data if employee_data else []# List of employee names.
        self.shift_names = shift_data if shift_data else []# List of shift names.
        self.unavailable_days = preferences['unavailable_days'] if preferences else {}# Dictionary to hold days an employee is unavailable. Key is employee index and value is list of days.
        self.shift_preferences = preferences['shift_preferences'] if preferences else {}# Dictionary to hold employee shift preferences. Key is employee index and value is another dictionary mapping day index to preference score.
        # Dictionary holding the seniority score of each employee. Key is employee index and value is seniority score.
        self.seniority = seniority if seniority else {}
        # List of lists. Each sublist represents a day, and contains the number of employees required for each shift on that day.
        self.shift_requirements = shift_requirements if shift_requirements else []

    

    def generate_schedule(self):
        """Generates the optimal schedule based on provided data."""
        num_employees = len(self.employee_names)
        num_days = 7
        num_shifts = len(self.shift_names)
        all_employees = range(num_employees)
        all_days = range(num_days)
        all_shifts = range(num_shifts)

        model = cp_model.CpModel()

        # Create binary variables to determine if an employee 'e' is working on a shift 's' on day 'd'.
        shifts = {}
        for e in all_employees:
            for d in all_days:
                for s in all_shifts:
                    shifts[(e, d, s)] = model.NewBoolVar('shift_e%id%is%i' % (e, d, s))

        # Variables to hold penalties for not meeting soft constraints.
        penalties = {}
        for e in all_employees:
            penalties[e] = model.NewIntVar(0, num_days, 'penalty_e%i' % e)

        # Hard constraints

        # Each shift is assigned to exactly one employee
        for d in all_days:
            for s in all_shifts:
                model.Add(sum(shifts[(e, d, s)] for e in all_employees) == self.shift_requirements[d][s])

        # Adds unavailable days
        for e, days in self.unavailable_days.items():
            for d in days:
                model.Add(sum(shifts[(e, d, s)] for s in all_shifts) == 0)

        # Each employee works at most one shift per day
        for e in all_employees:
            for d in all_days:
                model.Add(sum(shifts[(e, d, s)] for s in all_shifts) <= 1)

        # Each employee works at most five shifts per week
        for e in all_employees:
            total_shifts = sum(shifts[(e, d, s)] for d in all_days for s in all_shifts)
            model.Add(total_shifts <= 5)

        # Soft constraints

        # Each employee works at least two shifts per week
        for e in all_employees:
            total_shifts = sum(shifts[(e, d, s)] for d in all_days for s in all_shifts)
            # The penalty is the difference between 2 and the total number of shifts (if positive)
            model.Add(penalties[e] >= 2 - total_shifts)

        # Objective function

        # Preference score for the schedule
        default_preference = 1
        preference_score = sum(
            shifts[(e, d, s)] * self.shift_preferences.get(e, {}).get(d, default_preference)
            for e in all_employees for d in all_days for s in all_shifts
        )

        # Seniority score for the schedule
        seniority_score = sum(shifts[(e, d, s)] * self.seniority[e] for e in all_employees for d in all_days for s in all_shifts)

        # Penalty for not working at least two shifts per week
        total_penalty = sum(penalties[e] for e in all_employees)

        # The objective is to maximize the sum of the preference and seniority scores, minus the total penalty
        model.Maximize(preference_score + 2 * seniority_score - total_penalty)

        # Creates the solver and solve
        solver = cp_model.CpSolver()
        solver.Solve(model)

        # Build the schedule
        schedule = {}
        for d in all_days:
            schedule[d] = {}
            for s in all_shifts:
                for e in all_employees:
                    if solver.Value(shifts[(e, d, s)]) == 1:
                        schedule[d][s] = self.employee_names[e]

        # Build total shifts for each employee
        total_shifts_per_employee = {}
        for e in all_employees:
            total_shifts = sum(solver.Value(shifts[(e, d, s)]) for d in all_days for s in all_shifts)
            total_shifts_per_employee[self.employee_names[e]] = total_shifts

        return schedule, total_shifts_per_employee
    
    

def get_input_data():
    # Employees' names
    employee_names =  ["Dani Bricelo", "Ramon Ombrellino", "Robert Ima", 
                      "Jonathan Politz", "Lizbeth Santana", "Adelaide Albuquerque", 
                      "Francisco Moreno", "Christal Ankins", "Camila Rodriguez", 
                      "Stephanie Jonson", "Ty Miller", "Rocio Salto", "Melissa Doyle", 
                      "Larry Obregon", "facuendo farias","pepe salgado", "juan martin vargas", "pepe ongito"]
    # Shift names
    shift_names = ["Main Bar Opener", "Courtyard Opener", 
                   "Swing Inside", "Swing Outside", 
                   "Main Bar Closer", "Courtyard Closer", 
                   "Southwing Opener", "Southwing Closer", "Event"]
    unavailable_days = {12:[0,1]}  # Employees input days they can't work
    # Employees' shift preferences (higher is better): [morning, night, all_day]
    shift_preferences = {
        0: {},  
        2: {}, 
        3: {}, 
        4: {}, 
        5: {}, 
        6: {},
        7: {}, 
        8: {},  
        9: {4: 10}, #Empleado 9 tiene 10/10 ganas de trabajr dia 4
        10: {6:5}, #Empleado 10 tiene 5/10 ganas de trabajar dia 6
        11: {}, 
        12: {4: 10, 5: 10, 6:10}, 
        13: {}, 
        14: {},
        15:{}
        }
    # senority 
    seniority = {
    0: 10, 1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 
    8: 10, 9: 10, 10: 10, 11: 10, 12: 10, 13: 10, 14: 10, 15: 10, 16: 10, 17: 10
}   
    # Manager inputs number of employees needed for each shift on each day
    shift_requirements = [
            #main bar, Courtyard Opener, Swing Inside, Swing Outside, Main Bar Closer, Courtyard Closer, Southwing Opener, Southwing Closer, Event
            [1, 1, 1, 1, 1, 1, 1, 1, 0],  # Monday
            [1, 1, 1, 0, 1, 2, 1, 1, 1],  # Tuesday
            [1, 1, 0, 1, 1, 1, 1, 1, 0],  # Wednesday
            [1, 1, 1, 1, 1, 1, 1, 1, 0],  # Thursday
            [1, 1, 1, 0, 1, 1, 1, 2, 2],  # Friday
            [1, 1, 1, 1, 1, 1, 1, 1, 5],  # Saturday
            [0, 0, 0, 0, 0, 0, 1, 1, 1]   # Sunday
        ]
    
    return employee_names, shift_names, {'unavailable_days': unavailable_days, 'shift_preferences': shift_preferences}, seniority, shift_requirements


def main():
    employee_data, shift_data, preferences, seniority, shift_requirements = get_input_data()
    scheduler = Scheduler(employee_data, shift_data, preferences, seniority, shift_requirements)
    schedule, total_shifts_per_employee = scheduler.generate_schedule()

    for day, shifts in schedule.items():
        print(f"Day {day}")
        for shift, employee in shifts.items():
            print(f"  {scheduler.shift_names[shift]}: {employee}")

    for employee, total_shifts in total_shifts_per_employee.items():
        print(f"Total shifts for {employee}: {total_shifts}")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred while setting up the schedule: {e}")