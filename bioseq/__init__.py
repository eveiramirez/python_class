"""
PACKAGE NAME
        bioseq

VERSION
        [1.0]

PYTHON VERSION
        3.9

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

DESCRIPTION
        bioseq es una paqueteria que contiene distintas herramientas para
        el manejo de secuencias de DNA y proteina.

CATEGORY
        DNA
        Protein
        Sequence

"""

from .dna import (DNARecord)
from .protein import (ProteinRecord, three_to_one)
from .sequence import (Sequence, del_gap, ext_fasta_seqs)

__all__ = ['DNARecord', 'ProteinRecord', 'three_to_one', 'Sequence', 'del_gap', 'ext_fasta_seqs', ]
