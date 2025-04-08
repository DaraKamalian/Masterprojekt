from z3 import *

def validate_and_solve_smt(smt_input):
    
    try:
        solver = Solver()
        solver.from_string(smt_input)
        output = "SMT formula is valid."
        # print("SMT formula is valid.")

        result = solver.check()
        output += f"\nSatisfiability result: {result}"
        # print(f"Satisfiability result: {result}")

        if result == sat:
            output += f"\nModel: {solver.model()}" 
            # print(f"Model: {solver.model()}")

    except Exception as e:
        output = f"Error in SMT formula: {e}" 
        # print(f"Error in SMT formula: {e}")
    return output