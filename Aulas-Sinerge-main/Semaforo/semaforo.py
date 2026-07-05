import time


def mostrar_sinal(simbolo: str, mensagem: str, tempo_segundos: int) -> None:
    print(f"{simbolo} {mensagem}")
    time.sleep(tempo_segundos)


def semaforo_basico() -> None:
    while True:
        mostrar_sinal("🟢", "VERDE - carros podem passar", 3)
        mostrar_sinal("🟡", "AMARELO - atenção", 1)
        mostrar_sinal("🔴", "VERMELHO - pare", 3)
        print("--------------------------")


def semaforo_com_botao_pedestre() -> None:
    while True:
        # fluxo normal
        print("🟢 VERDE - carros podem passar")

        resposta = input("Algum pedestre apertou o botão? (s/n): ").strip().lower()

        if resposta == "s":
            print("Pedido recebido. Aguarde...")
            time.sleep(1)

            print("🟡 AMARELO - atenção")
            time.sleep(2)

            print("🔴 VERMELHO - carros parados")
            print("🚶 Pedestre pode atravessar")

            for numero in range(5, 0, -1):
                print(f"🚶 Pedestre pode atravessar: {numero}")
                time.sleep(1)

            print("Voltando ao fluxo normal...")
        else:
            print("Nenhum pedestre aguardando. Mantendo fluxo dos carros.")

        print("--------------------------")


def semaforo_duas_ruas() -> None:
    while True:
        print("Rua A: 🟢 VERDE")
        print("Rua B: 🔴 VERMELHO")
        time.sleep(3)

        print("Rua A: 🟡 AMARELO")
        print("Rua B: 🔴 VERMELHO")
        time.sleep(1)

        print("Rua A: 🔴 VERMELHO")
        print("Rua B: 🟢 VERDE")
        time.sleep(3)

        print("Rua A: 🔴 VERMELHO")
        print("Rua B: 🟡 AMARELO")
        time.sleep(1)

        print("--------------------------")


def main() -> None:
    print("=== Simulação de Semáforo (Robótica em Python) ===")
    print("Escolha uma opção:")
    print("1 - Semáforo básico (ciclo verde/amarelo/vermelho)")
    print("2 - Semáforo com botão do pedestre (input)")
    print("3 - Semáforo de duas ruas (nunca duas verdes ao mesmo tempo)")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        semaforo_basico()
    elif opcao == "2":
        semaforo_com_botao_pedestre()
    elif opcao == "3":
        semaforo_duas_ruas()
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()

