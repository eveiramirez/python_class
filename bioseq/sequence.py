"""
MODULE NAME
        sequence

VERSION
        [1.0]

PYTHON VERSION
        3.9

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

DESCRIPTION
        Modulo para el manejo de secuencias biologicas.

CATEGORY
        Sequence

"""

from re import match


# Crear la excepcion AmbiguousBaseError
class AmbiguousError(Exception):
    """Clase para el manejo de errores de distintos tipos."""
    pass


class Sequence(object):
    """
    Clase para el manejo de secuencias biologicas.

    Atributos
    ---------
    seq: Secuencia de monomeros.

    Metodos
    -------
    length(self)
        Obtiene la longitud de la secuencia

    elements_count(self)
        Obtiene la cantidad de cada uno de los distintos elementos
        de la secuencia en forma de lista

    """

    seq = ""

    def length(self):
        """Obtiene la longitud de la secuencia"""
        return len(self.seq)

    def elements_count(self):
        """
        Obtiene la cantidad de cada uno de los distintos elementos
        de la secuencia en forma de lista.
        """
        # Obtener elementos unicos
        elements = list(set(self.seq))
        elements_list = {}

        # Crear diccionario con la cantidad de cada elemento
        for element in elements:
            elements_list[element] = self.seq.count(element)
        return elements_list


def del_gap(seq):
    """Elimina gaps de la secuencia"""
    return seq.replace('-', '').replace('.', '')


def check_seq(seq, pattern):
    """Revisa si la secuencia es valida usando un patron obtenido de
     una expresion regular."""
    t_seq = del_gap(seq)
    if not match(pattern, t_seq):
        raise Exception(f"Secuencia no valida: '{seq}'")


def ext_fasta_seqs(path):
    """
    Obtiene las secuencias de un archivo fasta y las devuelve en una lista.
    """
    try:
        if path is None:
            raise AmbiguousError("Missing file")
        elif not match(r'^.+\.fasta$', path):
            raise AmbiguousError("Invalid file: The file is not a fasta file")
        else:
            # Abrir archivo y obtener lineas
            file = open(path)
            lines = file.readlines()
            file.close()

            # Crear lista para secuencias y variable index
            seq_list = []
            i = -1

            # Obtener secuencias
            for line in lines:
                # Anadir secuencia a la lista
                if line[0] == '>':
                    seq_list.append('')
                    i += 1
                    seq_list[i] = ''
                elif line != '\n':
                    # Eliminar espacios en blanco y digitos de la secuencia
                    line = line.replace(' ', '').replace('\n', '').replace('\r', '')
                    seq_list[i] += ''.join([char for char in line if not char.isdigit()])

            # Dar lista de las secuencias como resultado
            return seq_list

    # Imprimir el mensaje de error correspondiente
    except IOError as ex:
        print('File not found: ' + ex.strerror)
    except AmbiguousError as ex:
        print(ex.args[0])
