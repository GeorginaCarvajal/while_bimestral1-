# Ejemplo de un menu


num = int(input("Menu: 1(Ver numeros), 0(salir) "))
while num != 0:
    x = 0
    while x < 10:
        print("El valor de X es: ",x)
        x += 1

        print("Saliendo,,,")
        num = int(input("menu: 1(ver numeros), 0(salir)"))

print("Gracias")