import adivinhacao 
import forca

print("#################")
print("Bem vindo ao menu")
print("#################")

print("Qual jogo você quer jogar?")
print("Digite (1) Adivinhação ou (2) Forca")

jogo = int(input("Sua escolha foi?"   ))

if (jogo == 1):
    print("Você escolheu adivinhação")
    adivinhacao.jogar_adivinhacao()
else:
    print("Você escolheu Forca")
    forca.jogar_forca()