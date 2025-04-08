import os
import itertools

def extract_and_save_smt_pairs(directory, output_file="smt_pairs.txt"):
    """
    Extracts all .smt2 files from the given directory, generates unique pairs, and saves them to a file.

    Parameters:
    - directory (str): Path to the directory containing SMT formulas.
    - output_file (str): File to save the SMT pairs.
    """
    # Get all SMT files
    smt_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.smt2')]

    if len(smt_files) < 2:
        print("Not enough SMT formulas to create pairs.")
        return

    # Generate unique pairs
    pairs = list(itertools.combinations(smt_files, 2))

    # Save pairs to a file
    with open(output_file, "w") as f:
        for pair in pairs:
            f.write(f"{pair[0]} {pair[1]}\n")

    print(f"Saved {len(pairs)} SMT pairs to {output_file}")

# Example usage:
extract_and_save_smt_pairs("./semantic-fusion-seeds/QF_BV/sat")