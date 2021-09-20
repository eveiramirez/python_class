"""

NAME
        gb_file_data_extractor.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/blob/master/python2/tareas/gb_file_data_extractor.py

DESCRIPTION
        This program contains the resumen function, which obtains
        information from a genbank file and the genes indicated by a
        list of gene names given as input.

CATEGORY
        GenBank
        Sequence


"""

from Bio import SeqIO


def resumen(path: str, gene_list: list[str]):
    """Funcion que pide como input un path de tipo str, y una lista
    de nombres de genes de tipo list[str], la cual imprime lo
    siguiente:

    * Organismo
    * Version de la secuencia
    * Fuente del aislado
    * Pais
    * Para cada gen en la lista:

        * Nombre del gen
        * Los primeros 15 nucleotidos de ADN
        * Los primeros 15 nucleotidos de ARN
        * Los primeros 15 aminoacidos de proteina"""

    # Acceder a los records del archivo de genbank
    for gb_record in SeqIO.parse(path, "genbank"):
        # Imprimir organismo, version de la secuencia, fuente de
        # aislado y pais

        print("Organismo:", gb_record.annotations["organism"])
        print("Version de la secuencia:", gb_record.annotations[
            "sequence_version"])
        print("Fuente de aislado:", gb_record.features[0].qualifiers[
            "isolation_source"])
        print("Pais:", gb_record.features[0].qualifiers["country"])

        # Acceder a cada uno de los features que sean CDS
        for ft in gb_record.features[1:]:
            if ft.type == "CDS":
                # Acceder a cada gen de la lista de genes
                for i, gene in enumerate(gene_list, 1):
                    # Evaluar si el gen de la lista coincide con el CDS
                    if gene == ft.qualifiers["gene"][0]:
                        start = ft.location.nofuzzy_start
                        end = ft.location.nofuzzy_end
                        seq = gb_record.seq[start:end]

                        # Imprimir el nombre del gen, los primeros 15
                        # nucleotidos de ADN, los primeros 15
                        # nucleotidos de ARN y los primeros 15
                        # aminoacidos de proteina

                        print(f"gen_{i}: {gene}")
                        print(f"ADN: {seq[:15]}")
                        print(f"ARN: {seq[:15].replace('T', 'U')}")
                        print(f"Proteina: {ft.qualifiers['translation'][0][:15]}")
