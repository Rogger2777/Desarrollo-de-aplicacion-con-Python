from src.logico.PersistenciaTrabajador import PersistenciaTrabajador
from src.logico.PersistenciaBonificacion import PersistenciaBonificacion
from src.logico.PersistenciaDescuento import PersistenciaDescuento
from src.modelos.Trabajador import Trabajador
from src.modelos.Bonificacion import Bonificacion
from src.modelos.declarative_base import Session


def verDatos():
    trabajador = PersistenciaTrabajador()
    trabajador.verTrabajadores()
    bonificacion = PersistenciaBonificacion()
    bonificacion.verBonificaciones()
    descuento = PersistenciaDescuento()
    descuento.verDescuentos()
"""
def verTrabajadoresBonificacion():
    # create a new session
    session = Session()
    # 3 - extract all movies
    trabajadores = session.query(Trabajador).all()

    # Imprimir trabajadores
    print('\n### Todos los trabajadores:')
    for trabajador in trabajadores:
        print(f'Id: {trabajador.id} - Mes-Año: {trabajador.mesAnio} - Nombre: {trabajador.nombreTrabajador:25} - Sueldo básico: {trabajador.sueldoBasico}')
    print('')

    datosPagos = session.query(Bonificacion).join(Trabajador).all()

    for datosPago in datosPagos:
        print(f"Trabajador: {datosPago.trabajador.nombreTrabajador}, Horas Extra: {datosPago.horasExtra}, movilidad: {datosPago.movilidad}")

"""


def verTrabajadoresBonificacion():
    # create a new session
    session = Session()

    # Imprimir trabajadores
    print('\n### Todos los trabajadores:')
    trabajadores = session.query(Trabajador).all()
    for trabajador in trabajadores:
        print(
            f'Id: {trabajador.id} - Mes-Año: {trabajador.mesAnio} - Nombre: {trabajador.nombreTrabajador:25} - Sueldo básico: {trabajador.sueldoBasico}')

    # Consulta para obtener bonificaciones
    datosPagos = session.query(Trabajador, Bonificacion) \
        .outerjoin(Bonificacion) \
        .all()

    for trabajador, datosPago in datosPagos:
        if datosPago is not None:
            print(
                f"Bonificación para {trabajador.nombreTrabajador}: Horas Extra: {datosPago.horasExtra}, Movilidad: {datosPago.movilidad}")
        else:
            print(f"No hay bonificaciones para {trabajador.nombreTrabajador}")

if __name__ == '__main__':
    verTrabajadoresBonificacion()

