from calculator import add, divide,multiply, power, subtract

def main():
    print("Calculadora simple")
    print("1 - Sumar")
    print("2 - Dividir")
    print("3 - Multiplicar")
    print("4 - Potencia")
    print("5 - Restar")

    opcion = input("Elegí una opción: ")

    try:
        num1 = float(input("Ingresá el primer número: "))
        num2 = float(input("Ingresá el segundo número: "))
    except ValueError:
        print("Por favor, ingresá un número válido")
        return

    if opcion == "1":
        print(add(num1, num2))
    elif opcion == "2":
        try:
            print(divide(num1, num2))
        except ZeroDivisionError:
            print("No se puede dividir por cero")
    elif opcion == "3":
        print(multiply(num1, num2))
    elif opcion == "4":
        print(power(num1, num2))
    else:
        print(subtract(num1, num2))

if __name__ == "__main__":
    main()