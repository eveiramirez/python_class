import argparse
import re

"""

NAME
        rna_2_protein.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/blob/master/python_scripts/rna_2_protein.py

DESCRIPTION
        This program translates a mRNA sequence into a protein sequence

CATEGORY
        RNA
        Translation
        Protein sequence

USAGE
        python rna_2_protein.py [OPTIONS]

ARGUMENTS
        -h, --help          show this help message and exit
        -i, --input         RNA sequence

EXAMPLES
        Example 1: Run the program and give the rna sequence as input

        Usage: $ python rna_2_protein.py -i sequence

        Input:
        CUGACAUGAUGUCUCCUCCCACGAAAGGCCUAAGCUAGCCC

        Output:
        mRNA sequence = AUGAUGUCUCCUCCCACGAAAGGCCUAAGCUAG
        Protein sequence = MMSPPTKGLS


"""


# Revisar si la secuencia es valida
def check_seq(seq):
    # Dar un error si la secuencia no es de RNA
    if not re.search(r'[AUGC]', seq):
        raise TypeError("Invalid sequence: No bases found")

    # Dar un error si la secuencia de RNA contiene caracteres invalidos
    invalid_bases = re.findall(r'[^AUGC]', seq)
    if invalid_bases:
        raise TypeError(f'Ambiguous bases found: {invalid_bases}')


# Revisar si la secuencia es valida
def find_mrna(seq):
    # Definir la posicion inicial de la busqueda
    start_codon_pos = 0

    # Buscar la secuencia hasta que surja un error
    while True:
        # Verificar si existe un codon de inicio
        start_codon = re.search(r"AUG", seq[start_codon_pos:])
        if start_codon:
            # Definir la posicion de inicio de busqueda y del codon de inicio
            start_pos = start_codon.start()
            start_codon_pos += start_pos
            start_pos = start_codon_pos
        else:
            raise TypeError("No coding sequence found")

        # Buscar codones de paro con respecto al codon de inicio encontrado
        while start_pos != -1:
            # Verificar si existe codon de paro
            stop_codon = re.search(r"UAA|UAG|UGA", seq[start_pos+3:])
            if stop_codon:
                # Verificar si se encuentra en el mismo marco de lectura
                stop_codon_pos = stop_codon.start()+start_pos+3
                if (stop_codon_pos - start_codon_pos) % 3 == 0:
                    return seq[start_codon_pos:stop_codon_pos + 3]
                # Cambiar de posicion de busqueda
                start_pos = stop_codon_pos-2
            else:
                # Terminar la busqueda de codon de paro
                start_pos = -1

        # Cambiar de posicion de busqueda para el codon de inicio
        start_codon_pos += 1


# Crear la descripcion del programa
parser = argparse.ArgumentParser(description="Script that translates a mRNA sequence into a protein sequence")

# Anadir los argumentos
parser.add_argument("-i", "--input",
                    metavar="sequence",
                    type=str,
                    help="RNA sequence")

# Ejecutar el metodo parse_args()
args = parser.parse_args()

# Crear lista de codones
gencode = {
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AAC': 'N', 'AAU': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGU': 'S', 'AGA': 'R',
    'AGG': 'R', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CAC': 'H',
    'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
    'CGG': 'R', 'CGU': 'R', 'GUA': 'V', 'GUC': 'V', 'GUG': 'V',
    'GUU': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
    'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'UCA': 'S', 'UCC': 'S',
    'UCG': 'S', 'UCU': 'S', 'UUC': 'F', 'UUU': 'F', 'UUA': 'L',
    'UUG': 'L', 'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
    'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W'}

# Obtener secuencia de aminoacidos
try:
    # Revisar si la secuencia es valida
    rna_seq = args.input
    if len(rna_seq) > 10000:
        raise TypeError("Sequence exceeds the maximum length of 10 kb")
    check_seq(rna_seq)

    # Buscar la secuencia codificante
    mrna = find_mrna(rna_seq)

    # Traducir la secuencia
    aa_seq = ""
    n = 0
    mrna_sz = len(mrna)-3
    while n < mrna_sz:
        aa_seq += gencode[mrna[n:n+3]]
        n += 3

    # Imprimir el resultado
    print(f"mRNA sequence = {mrna}\nProtein sequence = {aa_seq}")

except TypeError as ex:
    raise SystemExit(ex.args[0])
