#Crea una lista de autos
autos = ["Fiat", "Renault", "Toyota", "Ford", "Chevrolet", "Audi"]
autos.append("Dodge")
autos.insert(2, "Ferrari")
del autos[1]
autos.insert(1, "Renault")
autos[2] = "Mercedez"
print(autos)

#Crear una Tuplas

colores = ("Amarillo", "Azul", "Verde", "Rojo")
print(colores)

#Verificar que un dato esté en la tupla o lista
print("Amarillo" in colores)
if "Amarillo" in colores:
    print("El amarillo si existe en la tupla")

print("Ford" in autos)

#Agregar una valor a la lista, cuando este dato no existe
if "Jaguar" in autos:
    print("La marca si existe")
else:
    autos.append("Jaguar")
    print("Este auto fue agregado")

print(autos)

#DICCIONARIOS

#Como crearlo
usuario = {"id":1, "name":"Andres", "edad": 39, "Casado":True}
print(usuario)
#Imprimir un "key" especifico
print(usuario["edad"])
print(usuario["Casado"])
#Agregar un nuevo "key" y su correspondiente valor. Si el Valor no existe lo creará. En caso de existir lo actualizará OJO
usuario["Apellido"]= "Hernández"
print(usuario)
#Sustituir un valor de una "key"
usuario ["Apellido"]= "Hernández Ortega"
print(usuario)
#Imprimir sólo los Keys del Diccionario
print(usuario.keys())
#Imprimir sólo los values del Diccionario
print(usuario.values())
#Vaciar el Diccionario
usuario.clear()
print(usuario)
#Eliminar un Diccionario
del usuario
print(usuario)
