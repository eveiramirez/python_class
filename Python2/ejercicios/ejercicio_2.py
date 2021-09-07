import re

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

# Ejercicio 2
filename = "../../src/class2/seq.nt.fa"
id_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))

for i in id_dict:
    print(">{}".format(i))
    sec = id_dict[i].seq
    for codon in re.findall(r".{3}", str(sec[1:len(sec)])):
        print(codon, end="\t")
    print("\n")

# Ejercicio 3
filename = "../../src/class2/sample.fastq"

for record in SeqIO.parse(filename, "fastq"):
    print(record.letter_annotations)
