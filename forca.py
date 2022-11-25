
def jogar_forca():
    print ("========================")
    print("Bem vindo ao jogo da forca")
    print ("========================")

palavra_secreta = "palavra"
letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]
enforcou = False
acertou = False

#Enquanto o False for verdade(true) o While irá rodar
while(not enforcou and not acertou):
    
    print(letras_acertadas)
    chute = input("Qual é a palavra?" )
    chute = chute.strip()  #Ignora os espaços no input ex: '  A  '

    index = 0
    for letra in palavra_secreta:  
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

    print(letras_acertadas)


print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_forca()