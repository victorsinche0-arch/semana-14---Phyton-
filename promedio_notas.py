def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) /3
    return promedio
print("===calculo del promedio de tres notas===")
nota1 = float(input(" Ingrese la primera nota"))
nota2 = float(input(" Ingrese la segunda nota"))
nota3 = float(input(" Ingrese la tercera nota"))
resultado = calcular_promedio(nota1, nota2, nota3)
print(f"el promedio de las tres notas es:{resultado: .2f}")
