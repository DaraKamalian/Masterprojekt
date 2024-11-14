import os
import json
import re

# Directory containing SMT-LIB Benchmarks
# https://github.com/testsmt/semantic-fusion-seeds
repo_dir = ''
data = []


def extract_variables(formula):

    pattern = r'\(declare-fun\s+([^\s]+)\s+\(\)\s+([^\)]+)\)'
    matches = re.findall(pattern, formula)

    return [(match[0], match[1]) for match in matches]


def read_smt_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()


for logic in os.listdir(repo_dir):
    logic_dir = os.path.join(repo_dir, logic)
    if os.path.isdir(logic_dir):

        for sat_status in ['sat', 'unsat']:
            status_dir = os.path.join(logic_dir, sat_status)
            if os.path.isdir(status_dir):

                smt_files = [f for f in os.listdir(status_dir) if f.endswith('.smt2')]
                # Pair each file with every other file in the same directory
                for i in range(len(smt_files)):
                    for j in range(i + 1, len(smt_files)):
                        file1 = smt_files[i]
                        file2 = smt_files[j]
                        filepath1 = os.path.join(status_dir, file1)
                        filepath2 = os.path.join(status_dir, file2)
                        
                        formula1 = read_smt_file(filepath1)
                        formula2 = read_smt_file(filepath2)
                        
                        variables1 = extract_variables(formula1)
                        variables2 = extract_variables(formula2)
                        
                        for var1 in variables1:
                            for var2 in variables2:
                                if var1[1] == var2[1]:  # Same type
                                    # Generate fusion and inversion functions
                                    fusion_function = f"z = {var1[0]} + {var2[0]}"
                                    inversion_functions = {
                                        f"r_{var1[0]}({var2[0]}, z)": f"z - {var2[0]}",
                                        f"r_{var2[0]}({var1[0]}, z)": f"z - {var1[0]}"
                                    }
                                    # Append to list
                                    data.append({
                                        "formula1": formula1,
                                        "formula2": formula2,
                                        "fusion_function": fusion_function,
                                        "inversion_functions": inversion_functions,
                                        "logic": logic,
                                        "satisfiability": sat_status.upper()
                                    })
                                    # print(data)

# Write to JSON file
with open('fusion_inversion_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)