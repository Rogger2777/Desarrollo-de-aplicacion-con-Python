from src.modelos.Trabajador import Trabajador
from src.modelos.declarative_base import session
import re
import datetime
from sqlalchemy import func #para validar si ya existe un trabajador

class PersistenciaTrabajador():

    def validar_nombre(self, nombre):
        # Validar que el nombre no contenga números ni caracteres especiales(pero si espacios entre nombres)
        return bool(re.match(r'^[a-zA-Z\s]+$', nombre))

    def registrarTrabajador(self, nombre: str, sueldo: float | int,
                            mesanio: str = datetime.datetime.now().strftime('%B %Y')):
        # Verificación de Tipo de datos
        if not isinstance(mesanio, str):
            return False

        if not isinstance(nombre, str):
            return False

        if not (isinstance(sueldo, float) or isinstance(sueldo, int)):
            return False

        # El software no deberá dejar campos vacíos en los nombres, al registrar el nombre del trabajador.
        if not nombre or nombre == '':
            return False

        # Validar nombre
        if not self.validar_nombre(nombre):
            return False

        # El software no deberá permitir el ingreso de sueldo básico negativo al registrar el sueldo.
        if sueldo < 0:
            return False

        # El software solo deberá permitir como máximo hasta 35 caracteres, al registrar el nombre del trabajador.
        if len(nombre) > 35:
            return False

        # El software no deberá permitir el ingreso de dos nombres iguales al registrar el nombre del trabajador
        busqueda = session.query(Trabajador).filter(Trabajador.nombreTrabajador == nombre).all()
        if len(busqueda) != 0:
            return False

        # Verificar si ya existe un trabajador con el mismo nombre
        trabajador_existente = session.query(Trabajador).filter(    #SQLAlchemy para comparar los nombres
        func.lower(Trabajador.nombreTrabajador) == func.lower(nombre)).first()
        if trabajador_existente:
            return False  # Ya existe un trabajador con el mismo nombre

        # AGREGAMOS AL TRABAJADOR
        trabajador = Trabajador(mesanio, nombre, sueldo)
        session.add(trabajador)
        session.commit()

        return True


    def existe_trabajador(self, nombre):
        # Verificar si ya existe un trabajador con el mismo nombre
        trabajador_existente = session.query(Trabajador).filter(    #SQLAlchemy para comparar los nombres
        func.lower(Trabajador.nombreTrabajador) == func.lower(nombre)).first()
        if trabajador_existente:
            return False  # Ya existe un trabajador con el mismo nombre


    def verTrabajadores(self):
        trabajadores = session.query(Trabajador).all()
        print('\n-------- TRABAJADORES REGISTRADOS --------')
        for trabajador in trabajadores:
            print(f'nombre: {trabajador.nombreTrabajador} sueldo: {trabajador.sueldoBasico}')
        print('')
