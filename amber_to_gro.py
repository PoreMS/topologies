import sys
import parmed as pmd

# Initialize
file_name = sys.argv[1]

# Load parameter
amber = pmd.load_file(file_name+".prmtop", file_name+".inpcrd")

# Save a GROMACS topology and GRO file
amber.save(file_name+".top")
amber.save(file_name+".gro")
