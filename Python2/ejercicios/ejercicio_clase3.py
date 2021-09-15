from Bio import SeqIO

# Ejercicio 4
for gb_record in SeqIO.parse("../../src/class2/virus.gb", "genbank"):
    print(gb_record.annotations["organism"],
          gb_record.annotations["sequence_version"])

# Ejercicio 5
for gb_record in SeqIO.parse("../../src/class2/virus.gb", "genbank"):
    print(gb_record.features[0].qualifiers["isolation_source"][0],
          gb_record.features[0].qualifiers["country"][0])

# Ejercicio 6
for gb_record in SeqIO.parse("../../src/class2/virus.gb", "genbank"):
    start = gb_record.features[10].location.nofuzzy_start
    end = gb_record.features[10].location.nofuzzy_end
    seq = gb_record.seq[start:end]
    print(seq)
    print(seq.replace('T', 'U'))
    print(gb_record.features[10].qualifiers["translation"][0])
