import random

mensagem_inicial = str("  Pronto para jogar Joken Pô?  ")
mensagem_inicial2= str("     Sente a pressão bebê")
numero_pc = 0
numero_pessoa = 4
escolha = 0
vitorias = 0
derrotas = 0 
nome_do_jogador = str
rank = 0
nivel = 0

def BoasVindas():
    global nome_do_jogador

    print("="*len(mensagem_inicial))
    print(mensagem_inicial)
    print(mensagem_inicial2)
    print("="*len(mensagem_inicial))
    nome_do_jogador = str(input("Insira seu nome: "))

def PessoaEscolha():
    global numero_pessoa, escolha

    numero_pessoa = int(input("Escolha:\n1-Pedra\n2-Papel\n3-Tesoura\n0-Sair\n"))
    if numero_pessoa == 1:
        escolha = str("Pedra")
    elif numero_pessoa == 2:
        escolha = str("Papel")
    elif numero_pessoa == 3:
        escolha = str("Tesoura")
    else:
        print("Fim de jogo!")

    print("Você escolheu {0} ".format(escolha))

def PCEscolha():
    global numero_pc

    numero_pc = random.randint(1,3)
    if numero_pc == 1:
        print("A maquina escolheu: Pedra")
    elif numero_pc == 2:
        print("A maquina escolheu: Papel")
    elif numero_pc == 3:
        print("A maquina escolheu: Tesoura")

def Resultados():
    global numero_pc, numero_pessoa, derrotas, vitorias, rank, nivel

    if numero_pc == numero_pessoa:
        print("Empate!")
    #Vitorias
    elif numero_pc == 1 and numero_pessoa == 2:
        print("Você ganhou!")
        vitorias = vitorias + 1 
    elif numero_pc == 2 and numero_pessoa == 3:
        print("Você ganhou!")
        vitorias = vitorias + 1 
    elif numero_pc == 3 and numero_pessoa == 1:
        print("Você ganhou!")
        vitorias = vitorias + 1 
    #Derrotas
    elif numero_pc == 1 and numero_pessoa == 3:
        print("Você perdeu!")
        derrotas = derrotas + 1
    elif numero_pc == 2 and numero_pessoa == 1:
        print("Você perdeu!")
        derrotas = derrotas + 1
    elif numero_pc == 3 and numero_pessoa == 2:
        print("Você perdeu!")
        derrotas = derrotas + 1
    #Começando a verificar o Rank do jogador
    rank = vitorias - derrotas
    
    if rank <= 10:
        nivel = str("Ferro")
    elif rank <= 11 and rank >= 20:
        nivel = str("Bronze")
    elif rank <= 21 and rank >= 50:
        nivel = str("Prata")
    elif rank <= 51 and rank >= 80:
        nivel = str("Ouro")
    elif rank <= 81 and rank >= 90:
        nivel = str("Diamante")
    elif rank <= 91 and rank >= 100:
        nivel = str("Lendário")
    else:
        nivel = str("Imortal")
        

BoasVindas()
while numero_pessoa!= 0:

    PessoaEscolha()
    if numero_pessoa == 0:
        break
    PCEscolha()
    Resultados()



print("O jogador {0} tem o Rank {1} possui {2} vitorias".format(nome_do_jogador, nivel, rank))