"""

NAME
        tarea_1.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/blob/master
        /python2/tareas/tarea_1.py

DESCRIPTION
        Este programa contiene la clase PolReg, que permite crear
        objetos que tengan atributos de poligonos regulares y obtener
        informacion acerca de ellos con sus metodos.

        Tambien se encuentran las subclases Cuadrado y Triangulo, las
        cuales contienen metodos mas especificos

CATEGORY
        Math
        Regular Polygon
        POO

"""


class PolReg(object):
    """
    Clase para la creacion de poligonos regulares.

    Atributos
    ---------
    no_lados: Numero de lados

    tam_lados: Tamano de los lados

    Metodos
    -------
    sum_ang_int(self)
        Obtiene la suma de angulos interiores en grados sexagesimales.

    ang_cent(self)
        Obtiene el valor del angulo central en grados sexagesimales.

    ang_int(self)
        Obtiene el valor del angulo interior en grados sexagesimales.

    ang_ext(self)
        Obtiene el valor del angulo exterior en grados sexagesimales.

    perimetro(self)
        Obtiene el perimetro.

    """

    def __init__(self, no_lados: float, tam_lados: float):
        self.no_lados = no_lados
        self.tam_lados = tam_lados

    def sum_ang_int(self):
        ang = 180*(self.no_lados-2)
        return ang

    def ang_cent(self):
        ang = 360 / self.no_lados
        return ang

    def ang_int(self):
        ang = 180 * (self.no_lados - 2)/self.no_lados
        return ang

    def ang_ext(self):
        ang_sup = self.ang_int()
        return 180 - ang_sup

    def perimetro(self):
        p = self.no_lados*self.tam_lados
        return p


class Cuadrado(PolReg):
    """
    Clase para la creacion de cuadrados.

    Metodos
    -------
    area(self)
        Obtiene el valor del area.

    """

    def __init__(self, tam_lados):
        PolReg.__init__(self, no_lados=4, tam_lados=tam_lados)

    def sum_ang_int(self):
        return 360

    def ang_cent(self):
        return 90

    def ang_int(self):
        return 90

    def ang_ext(self):
        return 90

    def perimetro(self):
        p = self.no_lados*4
        return p

    def area(self):
        a = self.tam_lados**2
        return a


class Triangulo(PolReg):
    """
        Clase para la creacion de cuadrados.

        Metodos
        -------
        area(self)
            Obtiene el valor del area.

    """

    def __init__(self, tam_lados):
        PolReg.__init__(self, no_lados=3, tam_lados=tam_lados)

    def sum_ang_int(self):
        return 180

    def ang_cent(self):
        return 120

    def ang_int(self):
        return 60

    def ang_ext(self):
        return 120

    def perimetro(self):
        p = self.no_lados * 3
        return p

    def area(self):
        a = (3**.5)*(self.tam_lados**2)/4
        return a
