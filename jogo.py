import jogoForca
import jogoAdivinhacao

def escolha_jogo():
    print("*********************************")
    print("Escolha o seu jogo!")
    print("*********************************")

    print("(1) Forca (2) Adivinhacao")

    jogo = int(input("Qual jogo voce quer jogar?"))

    if(jogo == 1):
        print("jogando forca")
        jogoForca.jogar()
    elif(jogo == 2):
        print("jogando adivinhacao")
        jogoAdivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()