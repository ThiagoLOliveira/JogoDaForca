import random as rd

listaPalavras = ['morango','abacate','tecnologia','matematica','jogo','participar','unico','calvo','churrasco','musica','filmes','futebol']
ac = 0
palavra = rd.choice(listaPalavras)
listaDesafio = ["_"] * len(palavra)
print(palavra)
while ac != 8:
    letra = str(input("Insira uma letra: ")).lower()
    if letra in palavra:
        print("Letra correta!")
        for i in range(len(palavra)):
            if palavra[i] == letra:
                listaDesafio[i] = letra
        print("Palavra atual:", " ".join(listaDesafio))
        if "_" not in listaDesafio:
            print("Parabéns! Você adivinhou a palavra!")
            break
    else:
        print("Letra incorreta. Tente novamente.")
        ac += 1
    ac += 1

