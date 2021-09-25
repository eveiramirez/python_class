"""

NAME
        get_pbd_file_residues.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/blob/master/Python2/tareas/get_pdb_file_residues.py

DESCRIPTION
        This program contains the get_residue function, which obtains
        residues of a chain from a pdb file and return them in a list.

CATEGORY
        Protein Data Bank
        Protein
        Sequence

EXAMPLES
    Example 1:  Run the program and give the file path, chain name,
    and residue name as input

            Usage: get_residue("1kcw.pdb", "A", "CYS")

            Input:
            1kcw.pdb path
            "A"
            "CYS"

            Output: [<Residue CYS het=  resseq=155 icode= >,
                    <Residue CYS het=  resseq=181 icode= >,
                    <Residue CYS het=  resseq=221 icode= >,
                    <Residue CYS het=  resseq=257 icode= >,
                    <Residue CYS het=  resseq=319 icode= >,
                    <Residue CYS het=  resseq=338 icode= >,
                    <Residue CYS het=  resseq=515 icode= >,
                    <Residue CYS het=  resseq=541 icode= >,
                    <Residue CYS het=  resseq=618 icode= >,
                    <Residue CYS het=  resseq=680 icode= >,
                    <Residue CYS het=  resseq=699 icode= >,
                    <Residue CYS het=  resseq=855 icode= >,
                    <Residue CYS het=  resseq=881 icode= >,
                    <Residue CYS het=  resseq=1021 icode= >]


"""

from Bio import PDB
from re import search


def get_residue(path: str, chain: str, residue: str):
    """Funcion que pide como input un path de tipo str de un archivo
    pdb, el nombre de una cadena de tipo str, y el nombre de un
    residuo de tipo str, devolviendo una lista de los residuos de esa
    cadena contenidos en el archivo pdb"""

    try:
        # Obtener nombre del archivo del path
        name = search(r'[^/]*pdb$', path)
        # Verificar si es un archivo pdb
        if name is None:
            raise SystemExit(f"El path = '{path}' "
                             f"no es de un archivo pdb")
        name = name.group(0)

        # Obtener estructura del archivo
        parser = PDB.PDBParser(QUIET=True)
        struc = parser.get_structure(name, path)

        # Obtener los residuos y guardarlos en la lista
        rs_chain = []
        for model in struc:
            for rs in model.child_dict[chain]:
                if rs.get_resname() == residue:
                    rs_chain.append(rs)
        return rs_chain

    except FileNotFoundError as ex:
        raise SystemExit("El archivo no se pudo abrir: "
                         + ex.strerror)


print(get_residue("../../src/class3/1kcw.pdb", "A", "CYS"))
