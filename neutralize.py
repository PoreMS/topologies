import sys
import parmed as pmd

# Initialize
file_name = sys.argv[1]

# Load parameter
res = pmd.load_file(file_name+".mol2")

# Fix charges and write mol2 file
res.fix_charges(precision=6)
res.save(file_name+".mol2")
