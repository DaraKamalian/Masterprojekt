from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["formula1", "formula2"],
    template="""
    You are tasked with automating the construction of fusion and inversion functions for arithmetic formulas using Semantic Fusion. 

    Background:
    1. **Fusion Function**: Combines variables from two formulas (x and y) into a new variable (z) while maintaining logical consistency.
    2. **Inversion Functions**: Recover the original variables (x and y) from the fused variable (z).
    3. **Fused Formula**: Combines the two formulas using the generated functions, preserving satisfiability or unsatisfiability.

    Example:
    Input Formulas:
    φ1: x > 0 ∧ x < 10
    φ2: y > -5 ∧ y < 5

    Fusion Function: f(x, y) = x + y
    Inversion Functions: r_x(y, z) = z - y, r_y(x, z) = z - x
    Fused Formula: (z - y > 0 ∧ z - y < 10) ∧ (z - x > -5 ∧ z - x < 5)

    Task:
    Generate a fusion function, inversion functions, and fused formula for the following inputs:
    φ1: {formula1}
    φ2: {formula2}

    Output the fusion function, inversion functions, and fused formula in SMT-LIB format.
    """
)