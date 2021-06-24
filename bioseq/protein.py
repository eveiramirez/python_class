"""
MODULE NAME
        protein

VERSION
        [1.0]

PYTHON VERSION
        3.9

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

DESCRIPTION
        Modulo para el manejo secuencias de proteinas.

CATEGORY
        Protein
"""

from .sequence import (Sequence, check_seq, del_gap)
from re import compile


class ProteinRecord(Sequence):
    """
    Clase para secuencias de proteinas. Contiene diferentes
    herramientas para obtener informacion de la secuencia.

    Atributos
    ---------
    seq: Secuencia de aminoacidos.

    Metodos
    -------
    one_to_three(self)
        Convierte de codigo de una letra a tres letras.

    prot_to_dna(self)
        Convierte la secuencia a DNA.

    """

    # Inicializar parametros
    def __init__(self, seq: str):
        self.seq = str(seq).upper()
        check_seq(self.seq, pattern)
        self.seq = del_gap(self.seq)

    # Transformar al codigo de tres letras
    def one_to_three(self):
        """Convierte de codigo de una letra a tres letras"""
        # Obtener elementos unicos
        seq_len = len(self.seq)
        t_seq = ''
        # Obtener del diccionario el codigo de tres letras
        for pos in range(0, seq_len):
            t_seq += aa_three_let[self.seq[pos]]
        return t_seq

    # Obtener secuencia de DNA
    def prot_to_dna(self):
        """Convierte la secuencia de aminoacidos a DNA"""
        # Obtener longitud de secuencia
        seq_len = len(self.seq)
        t_seq = ''
        # Obtener del diccionario los codones correspondientes
        for pos in range(0, seq_len):
            t_seq += aa_cons_codon[self.seq[pos]]
        return t_seq


def three_to_one(prot_seq):
    """
    Convierte una secuencia de aminoacidos en codigo de tres letras en una letra.
    """
    # Obtener longitud de secuencia
    seq_len = len(prot_seq)
    t_seq = ''
    # Devolver error si la secuencia no es valida
    if seq_len % 3 != 0:
        raise ValueError(f"Secuencia no valida")
    # Verificar si los aminoacidos existen en el diccionario del codigo de una letra
    for pos in range(0, seq_len-2, 3):
        # Devolver error si no existe el aminoacido
        if not prot_seq[pos:pos+3] in aa_one_let:
            raise ValueError(f"Secuencia no valida: El aminoacido {prot_seq[pos:pos+3]}"
                             f" no es valido")
    # Transformar al codigo de una letra
    for pos in range(0, seq_len - 2, 3):
        t_seq += aa_one_let[prot_seq[pos:pos+3]]
    return t_seq


pattern = compile(r'^[ARNDCEQGHILKMFPSTWYVXBZOU*.-]+$')

aa_three_let = {
    'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'C': 'Cys', 'E': 'Glu', 'Q': 'Gln', 'G': 'Gly',
    'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'F': 'Phe', 'P': 'Pro', 'S': 'Ser',
    'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val', 'X': 'Xaa', '*': 'Ter', 'B': 'Asx', 'Z': 'Glx',
    'O': 'Pyl', 'U': 'Sec',
}

aa_one_let = {
    'Ala': 'A', 'Arg': 'R', 'Asn': 'N', 'Asp': 'D', 'Cys': 'C', 'Glu': 'E', 'Gln': 'Q', 'Gly': 'G',
    'His': 'H', 'Ile': 'I', 'Leu': 'L', 'Lys': 'K', 'Met': 'M', 'Phe': 'F', 'Pro': 'P', 'Ser': 'S',
    'Thr': 'T', 'Trp': 'W', 'Tyr': 'Y', 'Val': 'V', 'Xaa': 'X', 'Ter': '*', 'Asx': 'B', 'Glx': 'Z',
    'Pyl': 'O', 'Sec': 'U',
}

aa_cons_codon = {
    'A': 'GCN', 'R': 'MGN', 'N': 'AAY', 'D': 'GAY', 'C': 'TGY', 'E': 'GAR', 'Q': 'CAR', 'G': 'GGN',
    'H': 'CAY', 'I': 'ATH', 'L': 'YTN', 'K': 'AAR', 'M': 'ATG', 'F': 'TTY', 'P': 'CCN', 'S': 'WSN',
    'T': 'ACN', 'W': 'TGG', 'Y': 'TAY', 'V': 'GTN', 'X': 'NNN', '*': 'TRR', 'B': 'RAY', 'Z': 'SAR',
    'O': 'UAG', 'U': 'UGA',
}
