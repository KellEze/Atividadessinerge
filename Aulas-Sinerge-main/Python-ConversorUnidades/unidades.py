def converter_temperatura():
    print("\n=== TEMPERATURA ===")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        c = float(input("Digite a temperatura em Celsius: "))
        f = c * 1.8 + 32
        print("Resultado:", f, "°F")

    elif opcao == "2":
        f = float(input("Digite a temperatura em Fahrenheit: "))
        c = (f - 32) / 1.8
        print("Resultado:", c, "°C")

    elif opcao == "3":
        c = float(input("Digite a temperatura em Celsius: "))
        k = c + 273.15
        print("Resultado:", k, "K")

    elif opcao == "4":
        k = float(input("Digite a temperatura em Kelvin: "))
        c = k - 273.15
        print("Resultado:", c, "°C")

    else:
        print("Opção inválida.")


def converter_distancia():
    print("\n=== DISTÂNCIA ===")
    print("1 - Metros para centímetros")
    print("2 - Centímetros para metros")
    print("3 - Quilômetros para metros")
    print("4 - Metros para quilômetros")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        m = float(input("Digite a distância em metros: "))
        cm = m * 100
        print("Resultado:", cm, "cm")

    elif opcao == "2":
        cm = float(input("Digite a distância em centímetros: "))
        m = cm / 100
        print("Resultado:", m, "m")

    elif opcao == "3":
        km = float(input("Digite a distância em quilômetros: "))
        m = km * 1000
        print("Resultado:", m, "m")

    elif opcao == "4":
        m = float(input("Digite a distância em metros: "))
        km = m / 1000
        print("Resultado:", km, "km")

    else:
        print("Opção inválida.")


def converter_area():
    print("\n=== ÁREA ===")
    print("1 - Metros quadrados para centímetros quadrados")
    print("2 - Centímetros quadrados para metros quadrados")
    print("3 - Metros quadrados para quilômetros quadrados")
    print("4 - Quilômetros quadrados para metros quadrados")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        m2 = float(input("Digite a área em m²: "))
        cm2 = m2 * 10000
        print("Resultado:", cm2, "cm²")

    elif opcao == "2":
        cm2 = float(input("Digite a área em cm²: "))
        m2 = cm2 / 10000
        print("Resultado:", m2, "m²")

    elif opcao == "3":
        m2 = float(input("Digite a área em m²: "))
        km2 = m2 / 1_000_000
        print("Resultado:", km2, "km²")

    elif opcao == "4":
        km2 = float(input("Digite a área em km²: "))
        m2 = km2 * 1_000_000
        print("Resultado:", m2, "m²")

    else:
        print("Opção inválida.")


def converter_tempo():
    print("\n=== TEMPO ===")
    print("1 - Horas para minutos")
    print("2 - Minutos para horas")
    print("3 - Minutos para segundos")
    print("4 - Segundos para minutos")
    print("5 - Dias para horas")
    print("6 - Horas para dias")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        h = float(input("Digite as horas: "))
        minutos = h * 60
        print("Resultado:", minutos, "min")

    elif opcao == "2":
        minutos = float(input("Digite os minutos: "))
        h = minutos / 60
        print("Resultado:", h, "h")

    elif opcao == "3":
        minutos = float(input("Digite os minutos: "))
        segundos = minutos * 60
        print("Resultado:", segundos, "s")

    elif opcao == "4":
        segundos = float(input("Digite os segundos: "))
        minutos = segundos / 60
        print("Resultado:", minutos, "min")

    elif opcao == "5":
        dias = float(input("Digite os dias: "))
        horas = dias * 24
        print("Resultado:", horas, "h")

    elif opcao == "6":
        horas = float(input("Digite as horas: "))
        dias = horas / 24
        print("Resultado:", dias, "dias")

    else:
        print("Opção inválida.")


# Desafio extra (mínimo duas novas conversões)

def converter_massa():
    print("\n=== MASSA (DESAFIO EXTRA) ===")
    print("1 - Quilogramas para gramas")
    print("2 - Gramas para quilogramas")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        kg = float(input("Digite os quilogramas: "))
        g = kg * 1000
        print("Resultado:", g, "g")

    elif opcao == "2":
        g = float(input("Digite as gramas: "))
        kg = g / 1000
        print("Resultado:", kg, "kg")

    else:
        print("Opção inválida.")


def menu_conversao_unidades():
    while True:
        print("\n=== CONVERSÃO DE UNIDADES ===")
        print("1 - Temperatura")
        print("2 - Distância")
        print("3 - Área")
        print("4 - Tempo")
        print("5 - Massa (desafio extra)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            while True:
                print("\n=== TEMPERATURA ===")
                print("1 - Celsius para Fahrenheit")
                print("2 - Fahrenheit para Celsius")
                print("3 - Celsius para Kelvin")
                print("4 - Kelvin para Celsius")
                print("5 - Retornar")
                sub = input("Escolha uma opção: ").strip()
                if sub == "5":
                    break
                if sub in {"1", "2", "3", "4"}:
                    # usa converter_temperatura() lendo opcao novamente
                    # para evitar duplicação, chamamos com base na opção.
                    # Reimplementação simples via if abaixo:
                    if sub == "1":
                        c = float(input("Digite a temperatura em Celsius: "))
                        f = c * 1.8 + 32
                        print("Resultado:", f, "°F")
                    elif sub == "2":
                        f = float(input("Digite a temperatura em Fahrenheit: "))
                        c = (f - 32) / 1.8
                        print("Resultado:", c, "°C")
                    elif sub == "3":
                        c = float(input("Digite a temperatura em Celsius: "))
                        k = c + 273.15
                        print("Resultado:", k, "K")
                    elif sub == "4":
                        k = float(input("Digite a temperatura em Kelvin: "))
                        c = k - 273.15
                        print("Resultado:", c, "°C")
                else:
                    print("Opção inválida.")

        elif opcao == "2":
            while True:
                print("\n=== DISTÂNCIA ===")
                print("1 - Metros para centímetros")
                print("2 - Centímetros para metros")
                print("3 - Quilômetros para metros")
                print("4 - Metros para quilômetros")
                print("5 - Retornar")
                sub = input("Escolha uma opção: ").strip()
                if sub == "5":
                    break
                if sub == "1":
                    m = float(input("Digite a distância em metros: "))
                    print("Resultado:", m * 100, "cm")
                elif sub == "2":
                    cm = float(input("Digite a distância em centímetros: "))
                    print("Resultado:", cm / 100, "m")
                elif sub == "3":
                    km = float(input("Digite a distância em quilômetros: "))
                    print("Resultado:", km * 1000, "m")
                elif sub == "4":
                    m = float(input("Digite a distância em metros: "))
                    print("Resultado:", m / 1000, "km")
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            while True:
                print("\n=== ÁREA ===")
                print("1 - Metros quadrados para centímetros quadrados")
                print("2 - Centímetros quadrados para metros quadrados")
                print("3 - Metros quadrados para quilômetros quadrados")
                print("4 - Quilômetros quadrados para metros quadrados")
                print("5 - Retornar")
                sub = input("Escolha uma opção: ").strip()
                if sub == "5":
                    break
                if sub == "1":
                    m2 = float(input("Digite a área em m²: "))
                    print("Resultado:", m2 * 10000, "cm²")
                elif sub == "2":
                    cm2 = float(input("Digite a área em cm²: "))
                    print("Resultado:", cm2 / 10000, "m²")
                elif sub == "3":
                    m2 = float(input("Digite a área em m²: "))
                    print("Resultado:", m2 / 1_000_000, "km²")
                elif sub == "4":
                    km2 = float(input("Digite a área em km²: "))
                    print("Resultado:", km2 * 1_000_000, "m²")
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "4":
            while True:
                print("\n=== TEMPO ===")
                print("1 - Horas para minutos")
                print("2 - Minutos para horas")
                print("3 - Minutos para segundos")
                print("4 - Segundos para minutos")
                print("5 - Dias para horas")
                print("6 - Horas para dias")
                print("7 - Retornar")
                sub = input("Escolha uma opção: ").strip()
                if sub == "7":
                    break
                if sub == "1":
                    h = float(input("Digite as horas: "))
                    print("Resultado:", h * 60, "min")
                elif sub == "2":
                    minutos = float(input("Digite os minutos: "))
                    print("Resultado:", minutos / 60, "h")
                elif sub == "3":
                    minutos = float(input("Digite os minutos: "))
                    print("Resultado:", minutos * 60, "s")
                elif sub == "4":
                    segundos = float(input("Digite os segundos: "))
                    print("Resultado:", segundos / 60, "min")
                elif sub == "5":
                    dias = float(input("Digite os dias: "))
                    print("Resultado:", dias * 24, "h")
                elif sub == "6":
                    horas = float(input("Digite as horas: "))
                    print("Resultado:", horas / 24, "dias")
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "5":
            converter_massa()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_conversao_unidades()

