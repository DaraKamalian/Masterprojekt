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

smt_formula = """
(set-info :smt-lib-version 2.6)
(set-logic QF_BV)
(set-info :source |
 Patrice Godefroid, SAGE (systematic dynamic test generation)
 For more information: http://research.microsoft.com/en-us/um/people/pg/public_psfiles/ndss2008.pdf
|)
(set-info :category "industrial")
(set-info :status unsat)
(declare-fun z () (_ BitVec 8))
(assert (or 
    (let ((?v_0 (bvand (bvand ((_ zero_extend 24) z) (_ bv255 32)) (_ bv31 32)))) 
        (let ((?v_1 (bvadd ?v_0 ((_ zero_extend 24) (_ bv1 8))))) 
            (let ((?v_2 (bvadd ?v_1 (_ bv267 32)))) 
                (and true 
                    (bvsle ?v_2 (_ bv122 32)) 
                    (not (= ?v_0 (_ bv4294967295 32))) 
                    (bvsle ?v_1 (_ bv30 32)) 
                    (bvsle (_ bv121 32) ?v_2) 
                    (bvsle (_ bv81 32) ?v_2) 
                    (bvslt (_ bv0 32) ?v_2)))))
    (let ((?v_0 (bvand (bvand ((_ zero_extend 24) z) (_ bv255 32)) (_ bv31 32)))) 
        (let ((?v_1 (bvadd ?v_0 ((_ zero_extend 24) (_ bv1 8))))) 
            (let ((?v_2 (bvadd ?v_1 (_ bv267 32)))) 
                (and true 
                    (bvslt ?v_2 (_ bv121 32)) 
                    (not (= ?v_0 (_ bv4294967295 32))) 
                    (bvsle ?v_1 (_ bv30 32)) 
                    (bvsle (_ bv81 32) ?v_2) 
                    (bvslt (_ bv0 32) ?v_2)))))))
(check-sat)
(exit)
"""

print(validate_and_solve_smt(smt_formula))