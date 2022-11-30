from classe_Mytube import *
sistema = Mytube()
def menu():
    print("1 - Baixar Vídeo\n"
        "2 - Baixar música\n"
        "0 - Sair\n")

def baixarVideo():
    link = input("Cole o link do vídeo: ")
    flag = sistema.informacoesVideo(link)
    print(flag)
    flag2 = sistema.qualidadesVideo()
    print(flag2)
    qualidade = input("Digite a qualidade: ")

    if qualidade == '1080p':
        sistema.baixar1080()
    elif qualidade == '720p':
        sistema.baixar720()
    elif qualidade == '480p':
        sistema.baixar480()
    elif qualidade == '360p':
        sistema.baixar360()
    elif qualidade == '240p':
        sistema.baixar240()
    elif qualidade == '144p':
        sistema.baixar144()

def main():
    
    menu()
    op = int(input("Digite a opção: "))
    if op == 0:
        return False
    elif op == 1:
        baixarVideo()
    elif op == 2:
       pass
    elif op == 3:
        pass
        # escolher destino de download

main()