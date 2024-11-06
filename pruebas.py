import os
from models.repository.departamentorepository import DepartamentoRepository

ruta = os.path.join('proyectos', 'micarpeta', 'db', 'dsklibrary.db')

repoDpto = DepartamentoRepository()

# dptos = repoDpto.get_all()
dpto1 = repoDpto.get_by_id(27)
# dpto2 = repoDpto.get_by_codigo('68')

# for dpto in dptos:
#    print(dpto)
#    print(type(dpto))
print(dpto1.get_nombre())
print(type(dpto1))
# print(dpto2)
