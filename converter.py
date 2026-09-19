TASA_DOLAR = 17.30

def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kilometros_a_millas(km):
    return km * 0.621371

def millas_a_kilometros(millas):
    return millas / 0.621371

def pesos_a_dolares(pesos):
    return pesos / TASA_DOLAR

def dolares_a_pesos(dolares):
    return dolares * TASA_DOLAR


def mostrar_menu():
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilómetros a Millas")
    print("4. Millas a Kilómetros")
    print("5. Pesos Mexicanos a Dólares")
    print("6. Dólares a Pesos Mexicanos")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            print("Programa finalizado.")
            break

        if opcion not in {"1", "2", "3", "4", "5", "6"}:
            print("Opción no válida.")
            continue

        try:
            valor = float(input("Ingresa el valor numérico: "))
        except ValueError:
            print("Error: debes ingresar un valor numérico.")
            continue

        if opcion == "1":
            resultado = celsius_a_fahrenheit(valor)
            unidad = "°F"
        elif opcion == "2":
            resultado = fahrenheit_a_celsius(valor)
            unidad = "°C"
        elif opcion == "3":
            resultado = kilometros_a_millas(valor)
            unidad = "millas"
        elif opcion == "4":
            resultado = millas_a_kilometros(valor)
            unidad = "km"
        elif opcion == "5":
            resultado = pesos_a_dolares(valor)
            unidad = "USD"
        else:
            resultado = dolares_a_pesos(valor)
            unidad = "MXN"

        print(f"Resultado: {resultado:.2f} {unidad}")


if __name__ == "__main__":
    main()
