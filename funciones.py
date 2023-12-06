from datetime import date
from src.modelos.Trabajador import Trabajador
from src.modelos.Bonificacion import Bonificacion
from src.modelos.Descuento import Descuento
from src.modelos.declarative_base import Base, engine, Session

# Genera la database schema
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# create a new session
session = Session()

# create trabajador
trabajador1 = Trabajador("December 2023", "Ernesto Torres Rojas", 3500)
trabajador2 = Trabajador("December 2023", "Maria Salomon Ortega", 3000)
trabajador3 = Trabajador("December 2023", "Elena Tarazona Castro", 5000)
trabajador4 = Trabajador("December 2023", "Sofia Peralta Romero", 2500)
trabajador5 = Trabajador("December 2023", "Carmen Martinez Torres", 4500)
trabajador6 = Trabajador("December 2023", "Isabel Justiano  Devora", 6500)
session.add(trabajador1)
session.add(trabajador2)
session.add(trabajador3)
session.add(trabajador4)
session.add(trabajador5)
session.add(trabajador6)

# Crea descuentos
descuento1 = Descuento(date(2023, 1, 2), 1, 10, trabajador1)
descuento2 = Descuento(date(2023, 1, 3), 1, 15, trabajador2)
descuento3 = Descuento(date(2023, 1, 2), 2, 10, trabajador3)
session.add(descuento1)
session.add(descuento2)
session.add(descuento3)


# Crea bonificaciones
bonificacion1 = Bonificacion(date(2023, 1, 1), 4, 1000, trabajador1)
session.add(bonificacion1)

session.commit()
session.close()