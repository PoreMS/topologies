import sys

with open(sys.argv[1]) as file_in:
    data = []
    is_atoms = False
    is_si = False

    for line in file_in:
        if is_atoms:
            if len(line.split()) == 0:
                break
            elif not ";" in line.split()[0]:
                if "CHARGESI" in line:
                    is_si = True
                else:
                    data.append(float(line.split()[6]))
        else:
            is_atoms = "[ atoms ]" in line

print(data)
print()
print("Molecule Charge = "+"%.5f" % sum(data))
print("Molecule Charge = "+str(sum(data)))
if is_si:
    print("Charge with Si  = "+"%.5f" % (sum(data)+0.32))
    print("Charge with Si  = "+str(sum(data)+0.32))
print()
