import porems as pms


oxy = pms.Molecule("oxygen", "OXY")

oxy.add("OX", [0.0, 0, 0])
oxy.add("OX", 0, r=0.123)

pms.Store(oxy).gro()
pms.Store(oxy).pdb()
