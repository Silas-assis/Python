
def jogar():
    print("*********************************")
    print("***Bem Vindo ao Jogo de Forca***!")
    print("*********************************")

    palavra_secreta = "banana".upper()
    
    #for padrão para adicionar "_" para cada letra da palavra.
    #letras_acertadas =[]
    #for letra in palavra_secreta: 
        #letras_acertadas.append("_")
    
    letras_acertadas = ["_" for letra in palavra_secreta] #for dentro da lista. List Comprehensions

    enforcou = False
    acertou = False 
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você Ganhou!")
    else:
        print("Você Perdeu!")

    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()