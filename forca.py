import random

def jogar_forca():
    
    imprime_mensagem_inicio()
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = substituição_acertos(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #Enquanto o False for verdade(true) o While irá rodar
    
    while(not enforcou and not acertou):
        
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1 
            
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas 
        
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

def imprime_mensagem_inicio():

    print ("========================")
    print("Bem vindo ao jogo da forca")
    print ("========================")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def substituição_acertos(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual é a letra?" )
    chute = chute.strip().upper()  #Ignora os espaços no input ex: '  A  '
    
    return chute

def marca_chute_correto(chute,letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:  
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1  

def imprime_mensagem_vencedor():
    print("Parabens você ganhou!")

def imprime_mensagem_perdedor():
    print("Que pena você perdeu!")


if(__name__ == "__main__"):
    jogar_forca()