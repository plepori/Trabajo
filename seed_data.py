from prueba.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", dni=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", dni=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", dni=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", dni=567567).save()

print("Se cargo con éxito los Familiares de pruebas")