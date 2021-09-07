from Bio.Seq import Seq
from Bio.SeqUtils import nt_search
from Bio import SeqIO

start_codon = Seq("ATG")
stop_codons = [Seq("TAA"), Seq("TAG"), Seq("TGA")]
dna = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")

start = nt_search(str(dna), start_codon)

for i in range(1, len(start)):
    sec_prot = dna[i:]
    print(sec_prot)
    proteina = sec_prot.translate(to_stop=True)
    print(proteina)

##Ejercicio 2
filename = "../../src/class2/"
