import jogo_forca   
import jogo_adivinhacao

print("***********************************")
print("*Qual jogo deseja você quer jogar?*")
print("***********************************")

print("(1) Forca, (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando Forca")
    jogo_forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação")
    jogo_adivinhacao.jogar()