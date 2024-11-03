import porems as pms


ethene = pms.Molecule("ethene", "2EN")

ethene.add("C", [0, 0, 0])
ethene.add("C", 0, r=0.1334)

ethene.add("H", 0, r=-0.109, theta= (180-121.3))
ethene.add("H", 0, r=-0.109, theta=-(180-121.3))
ethene.add("H", 1, r= 0.109, theta= (180-121.3))
ethene.add("H", 1, r= 0.109, theta=-(180-121.3))


pms.Store(ethene).gro()
pms.Store(ethene).pdb()
