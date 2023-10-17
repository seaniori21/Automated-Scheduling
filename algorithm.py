from ortools.sat.python import cp_model

def main(shift_requirements, unavailable_days, shift_preferences, seniority):
    # Data
    num_employees = 15  
    num_days = 7
    num_shifts = 9 
    all_employees = range(num_employees)
    all_days = range(num_days)
    all_shifts = range(num_shifts)

    # Employees' names
    employee_names = ["Dani Bricelo", "Ramon Ombrellino", "Robert Ima", "Jonathan Politz", "Lizbeth Santana", "Adelaide Albuquerque", "Francisco Moreno", "Christal Ankins", "Camila Rodriguez", "Stephanie Jonson", "Ty Miller", "Rocio Salto", "Melissa Doyle", "Larry Obregon", "Facundo Farias"]
    
    # Shift names
    shift_names = ["Main Bar Opener", "Courtyard Opener", "Swing Inside", "Swing Outside", "Main Bar Closer", "Courtyard Closer", "Southwing Opener", "Southwing Closer", "Event"]
    
    # Creates the model
    model = cp_model.CpModel()

    # Create shift variables
    shifts = {}
    for e in all_employees:
        for d in all_days:
            for s in all_shifts:
                shifts[(e, d, s)] = model.NewBoolVar('shift_e%id%is%i' % (e, d, s))
    
    # Create penalty variables for soft constraints
    penalties = {}
    for e in all_employees:
        penalties[e] = model.NewIntVar(0, num_days, 'penalty_e%i' % e)

    # Hard constraints

    # Each shift is assigned to exactly one employee
    for d in all_days:
        for s in all_shifts:
            model.Add(sum(shifts[(e, d, s)] for e in all_employees) == shift_requirements[d][s])

    # Adds unavailable days
    for e, days in unavailable_days.items():
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
        shifts[(e, d, s)] * shift_preferences.get(e, {}).get(d, default_preference)
        for e in all_employees for d in all_days for s in all_shifts
    )

    # Seniority score for the schedule
    seniority_score = sum(shifts[(e, d, s)] * seniority[e] for e in all_employees for d in all_days for s in all_shifts)

    # Penalty for not working at least two shifts per week
    total_penalty = sum(penalties[e] for e in all_employees)

    # The objective is to maximize the sum of the preference and seniority scores, minus the total penalty
    model.Maximize(preference_score + 2 * seniority_score - total_penalty)

    # Creates the solver and solve
    solver = cp_model.CpSolver()
    solver.Solve(model)

    # Print out the schedule
    for d in all_days:
        print('Day', d)
        for s in all_shifts:
            for e in all_employees:
                if solver.Value(shifts[(e, d, s)]) == 1:
                    print('  {} shift: {}'.format(shift_names[s], employee_names[e]))

    # Print out total shifts for each employee
    for e in all_employees:
        total_shifts = sum(solver.Value(shifts[(e, d, s)]) for d in all_days for s in all_shifts)
        print('Total shifts for {}: {}'.format(employee_names[e], total_shifts))
        
if __name__ == '__main__':
    try:
        # Manager inputs number of employees needed for each shift on each day
        #cada columna representa un turno, y el valor representa cuantos empleados en cada turno
        shift_requirements = [
            #main bar, Courtyard Opener, Swing Inside, Swing Outside, Main Bar Closer, Courtyard Closer, Southwing Opener, Southwing Closer, Event
            [1, 1, 1, 1, 1, 1, 1, 1, 0],  # Monday
            [1, 1, 1, 0, 1, 2, 1, 1, 1],  # Tuesday
            [1, 1, 0, 1, 1, 1, 1, 1, 0],  # Wednesday
            [1, 1, 1, 1, 1, 1, 1, 1, 0],  # Thursday
            [1, 1, 1, 0, 1, 1, 1, 2, 2],  # Friday
            [1, 1, 1, 1, 1, 1, 1, 1, 5],  # Saturday
            [0, 0, 0, 0, 0, 0, 0, 0, 0]   # Sunday
        ]
        unavailable_days = {12:[0,1,2,3,4,6], 14: [0,2,4,5,6]}  # Employees input days they can't work
    
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
            }
        # senority 
        seniority = [3, 1, 5, 4, 2, 8, 1, 4, 1, 10, 10, 1, 10, 4, 8]
    
        main(shift_requirements, unavailable_days, shift_preferences, seniority)
    except Exception as e:
        print(f'An error occurred while setting up the schedule: {e}')