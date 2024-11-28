def generate_fusion_function(x_formula, y_formula):
    # Parse the input formulas
    x_var = 'x'
    y_var = 'y'

    if '>' in x_formula:
        x_min = 1
    else:
        x_min = float('-inf')

    if '<=' in x_formula:
        x_max = 5
    else:
        x_max = float('inf')

    if '<' in y_formula:
        y_min = 0
    else:
        y_min = float('-inf')

    if '>=' in y_formula:
        y_max = -3
    else:
        y_max = float('inf')

    # Generate the fusion function
    def f(x, y):
        return x + y

    return f


def generate_inversion_functions(fusion_function, x_var, y_var):
    # Parse the input formulas
    if '>' in x_formula:
        x_min = 1
    else:
        x_min = float('-inf')

    if '<=' in x_formula:
        x_max = 5
    else:
        x_max = float('inf')

    if '<' in y_formula:
        y_min = 0
    else:
        y_min = float('-inf')

    if '>=' in y_formula:
        y_max = -3
    else:
        y_max = float('inf')

    # Generate the inversion functions
    def r_x(y, z):
        return z - y

    def r_y(x, z):
        return z - x

    return r_x, r_y


def generate_fused_formula(fusion_function, x_var, y_var):
    # Generate the fused formula
    def f(z):
        if '>' in x_formula:
            return (z > x_min) and (z <= x_max)
        else:
            return z >= x_min

        if '<' in y_formula:
            return (z < y_min) and (z >= y_max)
        else:
            return z <= y_max

    return f


# Input Formulas
x_formula = 'x > 1 ∧ x ≤ 5'
y_formula = 'y < 0 ∧ y ≥ -3'

# Generate the fusion function
f = generate_fusion_function(x_formula, y_formula)

# Generate the inversion functions
r_x, r_y = generate_inversion_functions(f, 'x', 'y')

# Generate the fused formula
fused_formula = generate_fused_formula(f, 'x', 'y')

# Print the results
print('1. Fusion Function:', f.__name__)
print('2. Inversion Functions:')
print('•  r_x(y, z) =', r_x.__name__)
print('•  r_y(x, z) =', r_y.__name__)
print('3. Fused Formula (SMT-LIB):')
print('(declare-fun z () [Real/Int])')
print('(assert (and [')
for var in ['z > x_min', 'z <= x_max', 'z < y_min', 'z >= y_max']:
    print(var)
print('])')