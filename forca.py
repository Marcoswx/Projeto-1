
def jogar_forca():
    print ("========================")
    print("Bem vindo ao jogo da forca")
    print ("========================")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_",]
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #Enquanto o False for verdade(true) o While irá rodar
    
    while(not acertou and not enforcou):
        
        chute = input("Qual é a letra?" )
        chute = chute.strip().upper()  #Ignora os espaços no input ex: '  A  '
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:  
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas #esqueci de colocar o "not" então o laço não se formou
        print(letras_acertadas)


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_forca()