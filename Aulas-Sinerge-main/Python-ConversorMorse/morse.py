# Conversor de texto para Morse + decodificador (Morse -> texto)

codigo_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

# Invertendo a tabela para decodificação
morse_para_texto = {codigo: letra for letra, codigo in codigo_morse.items()}


def converter_para_morse(texto: str) -> str:
    """Texto -> Morse.

    Regras:
    - espaço em texto vira "/" no Morse
    - caracteres desconhecidos viram "?"
    - letras minúsculas são convertidas para maiúsculas
    """

    texto = texto.upper()
    resultado = []

    for caractere in texto:
        if caractere == " ":
            resultado.append("/")
        elif caractere in codigo_morse:
            resultado.append(codigo_morse[caractere])
        else:
            resultado.append("?")

    # No enunciado, o exemplo separa por espaço
    return " ".join(resultado)


def decodificar_morse(mensagem_morse: str) -> str:
    """Morse -> Texto.

    Regras:
    - separa letras por espaços
    - "/" representa espaço entre palavras
    - códigos desconhecidos viram "?"
    """

    partes = mensagem_morse.strip().split()
    resultado = []

    for codigo in partes:
        if codigo == "/":
            resultado.append(" ")
        elif codigo in morse_para_texto:
            resultado.append(morse_para_texto[codigo])
        else:
            resultado.append("?")

    return "".join(resultado).replace("  ", " ")


def menu() -> None:
    print("=== Conversor de Código Morse ===")
    print("1 - Converter texto para Morse")
    print("2 - Decodificar Morse para texto")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        mensagem = input("Digite a mensagem original (use letras/números e espaços): ")
        print("Mensagem em Morse:")
        print(converter_para_morse(mensagem))

    elif opcao == "2":
        mensagem = input(
            "Digite a mensagem em Morse (use pontos/traços e espaços; use / para separar palavras): "
        )
        print("Mensagem decodificada:")
        print(decodificar_morse(mensagem))

    else:
        print("Opção inválida.")


if __name__ == "__main__":
    menu()

