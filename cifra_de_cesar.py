# Cifra de César
# Criptografar texto
from art import logo

alfabeto = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def cesar(texto_inicial, qtd_deslocamento, direcao_cifra):
    texto_final = ""
    if direcao_cifra == "decode":
        qtd_deslocamento *= -1
    for letra in texto_inicial:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            nova_posicao = posicao + qtd_deslocamento
            texto_final += alfabeto[nova_posicao]
        else:
            texto_final += letra

    print(f"O texto foi {direcao}d para {texto_final}")


print(logo)
terminar = False
while not terminar:
    direcao = input("digite code para criptografar decode para descriptografar \n")
    texto = input("Digite a sua menssagem: \n ").lower()
    deslocamento = int(input("Digite o número da troca: \n"))

    deslocamento = deslocamento % 26

    cesar(texto, deslocamento, direcao)
    resetar = input("Digite 's' para continuar ou 'n' para sair do programa. ")
    if resetar == "n":
        terminar = True
        print("Obrigado por usar o Cifra César")
