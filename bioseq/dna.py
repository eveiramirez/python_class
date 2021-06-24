"""
MODULE NAME
        dna

VERSION
        [1.0]

PYTHON VERSION
        3.9

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

DESCRIPTION
        Modulo para el manejo secuencias de DNA.

CATEGORY
        DNA
"""

from .sequence import (Sequence, del_gap, check_seq)
from re import compile


class DNARecord(Sequence):
    """
    Clase para secuencias de DNA que acepta nucleotidos ambiguos.
    Contiene diferentes herramientas para obtener informacion de
    la secuencia.

    Atributos
    ---------
    seq: Secuencia de nucleotidos.

    Metodos
    -------
    get_kmers(self, k)
        Obtiene los kmers de una secuencia dada una longitud k.

    dna_to_protein(self)
        Convierte la secuencia de DNA a proteina.

    rev_comp(self)
        Obtiene la cadena complementaria reversa.

    dna_to_rna(self)
        Convierte la secuencia a RNA.

    at_content(self)
        Obtiene el contenido de AT.

    gc_content(self)
        Obtiene el contenido de GC.
    """

    # Inicializar parametros
    def __init__(self, seq: str):
        self.seq = str(seq).upper()
        check_seq(self.seq, pattern)
        self.seq = del_gap(self.seq)

    # Obtener k-mers
    def get_kmers(self, k):
        """Obtiene los kmers de una secuencia dada una longitud k."""
        # Obtener k y longitud
        k = str(k)
        length = len(self.seq)
        # Verificar si es digito
        if k.isdigit():
            k = int(k)
            # Verificar si esta dentro de los limites
            if 0 < k <= length:
                # Obtener kmers
                kmers = [self.seq[i: i + k] for i in range(0, len(self.seq) - k + 1)]
                return kmers
            else:
                raise ValueError(f"La longitud de k = {k} es igual a cero o mayor a la longitud "
                                 f"de la secuencia")
        else:
            raise TypeError(f"La longitud de k = '{k}' no es valida")

    # Obtener secuencia de aminoacidos
    def dna_to_prot(self):
        """Convierte la secuencia de DNA a proteina."""
        # Obtener longitud y crear secuencia transformada
        seq_len = len(self.seq)
        t_seq = ''
        # Obtener los codones cada 3 caracteres
        for pos in range(0, seq_len-2, 3):
            # Obtener el codon del diccionario, y si no poner 'X'
            if self.seq[pos:pos+3] in codon:
                t_seq += codon[self.seq[pos:pos+3]]
            else:
                t_seq += 'X'
        return t_seq

    # Obtener cadena complementaria reversa
    def rev_comp(self):
        """Obtiene la cadena complementaria reversa."""
        # Obtener elementos unicos
        nt_list = list(set(self.seq))
        t_seq = self.seq
        # Reemplazar los nucleotidos con el diccionario
        for nt in nt_list:
            t_seq = t_seq.replace(nt, complement[nt])
        # Devolver en mayusculas
        t_seq = t_seq.upper()
        return t_seq

    # Transformar la secuencia a RNA
    def dna_to_rna(self):
        """Convierte la secuencia a RNA."""
        return self.seq.replace('T', 'U')

    # Obtener contenido de AT
    def at_content(self):
        """Obtiene el contenido de AT."""
        # Obtener cantidad de AT y GC
        at_cont = self.seq.count('A') + self.seq.count('T')
        gc_cont = self.seq.count('G') + self.seq.count('C')
        return at_cont/(at_cont+gc_cont)

    # Obtener contenido de GC
    def gc_content(self):
        """Obtiene el contenido de GC."""
        # Obtener cantidad de AT y GC
        at_cont = self.seq.count('A') + self.seq.count('T')
        gc_cont = self.seq.count('G') + self.seq.count('C')
        return gc_cont/(at_cont+gc_cont)


pattern = compile(r'^[ATCGMRWSYKVHDBN.-]+$')

codon = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'TTY': 'F', 'TTR': 'L', 'CTM': 'L', 'CTR': 'L', 'CTW': 'L', 'CTS': 'L', 'CTY': 'L', 'CTK': 'L',
    'CTV': 'L', 'CTH': 'L', 'CTD': 'L', 'CTB': 'L', 'CTN': 'L', 'ATM': 'I', 'ATW': 'I', 'ATY': 'I',
    'ATH': 'I', 'GTM': 'V', 'GTR': 'V', 'GTW': 'V', 'GTS': 'V', 'GTY': 'V', 'GTK': 'V', 'GTV': 'V',
    'GTH': 'V', 'GTD': 'V', 'GTB': 'V', 'GTN': 'V', 'TCM': 'S', 'TCR': 'S', 'TCW': 'S', 'TCS': 'S',
    'TCY': 'S', 'TCK': 'S', 'TCV': 'S', 'TCH': 'S', 'TCD': 'S', 'TCB': 'S', 'TCN': 'S', 'CCM': 'P',
    'CCR': 'P', 'CCW': 'P', 'CCS': 'P', 'CCY': 'P', 'CCK': 'P', 'CCV': 'P', 'CCH': 'P', 'CCD': 'P',
    'CCB': 'P', 'CCN': 'P', 'ACM': 'T', 'ACR': 'T', 'ACW': 'T', 'ACS': 'T', 'ACY': 'T', 'ACK': 'T',
    'ACV': 'T', 'ACH': 'T', 'ACD': 'T', 'ACB': 'T', 'ACN': 'T', 'GCM': 'A', 'GCR': 'A', 'GCW': 'A',
    'GCS': 'A', 'GCY': 'A', 'GCK': 'A', 'GCV': 'A', 'GCH': 'A', 'GCD': 'A', 'GCB': 'A', 'GCN': 'A',
    'TAY': 'Y', 'TAR': '*', 'CAY': 'H', 'CAR': 'Q', 'AAY': 'N', 'AAR': 'K', 'GAY': 'D', 'GAR': 'E',
    'TGY': 'C', 'CGM': 'R', 'CGR': 'R', 'CGW': 'R', 'CGS': 'R', 'CGY': 'R', 'CGK': 'R', 'CGV': 'R',
    'CGH': 'R', 'CGD': 'R', 'CGB': 'R', 'CGN': 'R', 'AGY': 'S', 'AGR': 'R', 'GGM': 'G', 'GGR': 'G',
    'GGW': 'G', 'GGS': 'G', 'GGY': 'G', 'GGK': 'G', 'GGV': 'G', 'GGH': 'G', 'GGD': 'G', 'GGB': 'G',
    'GGN': 'G', 'RAY': 'B', 'SAR': 'Z',
}

complement = {
    'A': 't', 'C': 'g', 'G': 'c', 'T': 'a', 'M': 'k', 'R': 'y', 'W': 'w', 'S': 's',
    'Y': 'r', 'K': 'm', 'V': 'b', 'H': 'd', 'D': 'h', 'B': 'v', 'N': 'n',
}
