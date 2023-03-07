import random
import time
import jogo_superTrunfo.bibiJogo

#inicio do jogo(regras)
a=0
regras = jogo_superTrunfo.bibiJogo.regras(a)
continuar= "sim"
#Repetição
while(continuar.upper() == "SIM"):
#Chamadas das funções para iníciar o jogo
  baralho =jogo_superTrunfo.bibiJogo.baralho(a)
  cartasJ1 = jogo_superTrunfo.bibiJogo.cartasJogadores(baralho)
  cartasJ2 = jogo_superTrunfo.bibiJogo.cartasJogadores(baralho)
  novoBaralho = jogo_superTrunfo.bibiJogo.novoBaralho(baralho,cartasJ1,cartasJ2)
  pontosJ1=1000
  pontosJ2=1000
  
#For para jogadas
  for i in range(4):
    print("-"*60)
    if(i%2 != 0):
        print("Vez do jogador 2 desafiar")
    else:
        print("Vez do jogador 1 desafiar" )    
    print("-"*60)
    
#Input para selecionar o desafio
    desafio=input("\nEscolha o desafio entre: Agilidade, Força ou Inteligência: ")
#Contagem de pontos e rodadas 
    rodada= jogo_superTrunfo.bibiJogo.desafios(desafio,cartasJ1[i],cartasJ2[i])
    print("\n\nCarta do jogador 1: ",cartasJ1[i],"\n\nCarta do jogador 2: ",cartasJ2[i])
    pontos=jogo_superTrunfo.bibiJogo.contaPontos(pontosJ1,pontosJ2,rodada)
    pontosJ1=pontos[0]
    pontosJ2=pontos[1]
    
#Para verificar qual jogador ganhou 
    if(rodada[0]=="jogador 1"):
     
      print("\n",rodada[0].upper(),"GANHOU ESSA RODADA")
      cartasJ1.append(cartasJ2[i])
      cartasJ2.remove(cartasJ2[i])
      cartasJ2.insert(i,["."])
     
      
    elif(rodada[0]=="jogador 2"):

      print("\n",rodada[0].upper(),"GANHOU ESSA RODADA\n")
      cartasJ2.append(cartasJ1[i])
      cartasJ1.remove(cartasJ1[i])
      cartasJ1.insert(i,["."])
      cartasJ2.append(cartasJ1[i])
      
    else:
      print("EMPATE!")

    #Nova carta em caso de empate 
    if(pontos[2] == -1):
      print("\nAs cartas serão descartadas e cada jogador receberá uma nova")
      cartasJ1.remove(cartasJ1[i])
      cartasJ2.remove(cartasJ2[i])
      novaCartaJ1 = random.choice(novoBaralho)
      novaCartaJ2 = random.choice(novoBaralho)
      cartasJ1.insert(0,novaCartaJ1)
      cartasJ2.insert(0,novaCartaJ2)
      novoBaralho = jogo_superTrunfo.bibiJogo.novoBaralho(baralho,cartasJ1,cartasJ2)
  ganhador=jogo_superTrunfo.bibiJogo.ganhador(pontosJ1,pontosJ2)
  print(ganhador)
  continuar= input("Deseja reiniciar o jogo? ")
      

  
