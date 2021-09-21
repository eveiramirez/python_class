from Bio import PDB

# EJERCICIO 1
parser = PDB.PDBParser(QUIET=True)
struc = parser.get_structure("prot_1fat", "../../src/class3/1kcw.pdb")

print(struc.header['structure_method'])
print(struc.header['resolution'])

print(len(struc))

# EJERCICIO 2
for model in struc:
    for residue in model.child_dict["A"]:
        if residue.get_resname() == "CYS":
            print(residue)
