#Ingresar nombre y apellido del alumno, y sus notas de matemáticas, física y literatura
#Imprimir nombre, apellido y promedio
#Si el promedio es mayor a 6, imprimir "APROBADO"
#Si el promedio es menor a 4, imprimir "INSUFICIENTE"
#Si el promedio es 4 y 5.99, imprimir "A RECUPERATORIO"
# En caso de tener 9 o mas, imprimir "ALUMNO DESTACADO" esto aparte de "APROBADO"

nombre_apellido = input("Ingresa tu nombre y apellido: ")
matematicas = float(input("Ingresa la nota de Matemáticas: "))
fisica = float(input("Ingresa la nota de Física: "))
literatura = float(input("Ingresa la nota de Literatura: "))
promedio = (fisica+matematicas+literatura)/3
print("Hola "+nombre_apellido)
print("El promedio de tus notas es de:",promedio)
if promedio>6:
    print("TE FELICITO ESTAS APROBADO")
    if promedio>=9:
        print("Y ERES UN ALUMNO DESTACADO")
elif promedio<4:
    print("LO SIENTO ES INSUFICIENTE")
elif promedio>=4 <=5.99999:
    print("MALA SUERTE TENDRÁS QUE IR A RECUPERATORIO")
