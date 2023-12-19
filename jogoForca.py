def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

#enquanto true 
    while(not enforcou and not acertou):

        chute = input("Qual letra??")
        #devolvendo a minha string sem espaços
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            #upper()deixando a minha letra em maiuscula
            if(chute.upper() == letra.upper()):
                print(f"encontrei a letra {letra} na posicao {index}")
            index+=1

        print("jogando...")

    print("Fim do jogo")   
     
if(__name__ == "__main__"):
    jogar()


