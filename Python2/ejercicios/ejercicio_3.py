from Bio import SeqIO

# Ejercicio 4
for gb_record in SeqIO.parse("../../src/class2/virus.gb", "genbank"):
    print(gb_record.annotations["organism"],
          gb_record.annotations["sequence_version"])

# Ejercicio 5
for gb_record in SeqIO.parse("../../src/class2/virus.gb", "genbank"):
    print(gb_record.features[0].qualifiers["isolation_source"][0],
          gb_record.features[0].qualifiers["country"][0])

# Ejercicio 6 No acabado aun
for gb_record in SeqIO.parse("../../src/class2/virus.gb", "genbank"):
    print(gb_record.features)
