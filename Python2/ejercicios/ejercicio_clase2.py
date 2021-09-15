import re

from Bio.Seq import Seq
from Bio.SeqUtils import nt_search
from Bio import SeqIO

# Ejercicio 1
start_codon = Seq("ATG")
stop_codons = [Seq("TAA"), Seq("TAG"), Seq("TGA")]
dna = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTT"
          "TTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")

start = nt_search(str(dna), start_codon)

for i in range(1, len(start)):
    sec_prot = dna[i:]
    x = len(sec_prot) % 3

    # Se anade Ns al final para que sea multiplo de 3
    if x:
        sec_prot += (3-x)*"N"

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
# Obtener numero de lecturas cuyo promedio de calidad sea menor a un
# umbral dado
filename = "../../src/class2/sample.fastq"
mala_calidad = []
umbral = 40

for record in SeqIO.parse(filename, "fastq"):
    promedio = sum(record.letter_annotations["phred_quality"])/len(
        record.letter_annotations["phred_quality"])
    if promedio < umbral:
        mala_calidad.append((promedio, record.letter_annotations))

print(len(mala_calidad))

# Ejercicio 3.1
# Obtener lecturas cuyo promedio de calidad sea mayor a un
# umbral dado
filename = "../../src/class2/sample.fastq"
buena_calidad = []
umbral = 40

for record in SeqIO.parse(filename, "fastq"):
    promedio = sum(record.letter_annotations["phred_quality"])/len(
        record.letter_annotations["phred_quality"])
    if promedio > umbral:
        buena_calidad.append((promedio, record.letter_annotations))

print(buena_calidad)
