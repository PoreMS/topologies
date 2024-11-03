import copy
import porems as pms


kation = pms.Molecule("mo1_kation", "MO3K", "mo1_kation.gro")
anion  = pms.Molecule("mo1_anion",  "MO3A", "mo1_anion.gro")

anion.move(0, kation.pos(1))
anion.translate([0, -1, -1])

for atom in anion.get_atom_list():
    atom.set_residue(1)

mo1 = pms.Molecule("mo3", "MO3", [kation, anion])
mo1.zero()
pms.Store(mo1).gro(use_atom_names=True)
