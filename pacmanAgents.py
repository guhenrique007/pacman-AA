# pacmanAgents.py
# ---------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from pacman import Directions
from game import Agent
import random
import game
import util

class LeftTurnAgent(game.Agent):
  "An agent that turns left at every opportunity"
  
  def getAction(self, state):
    legal = state.getLegalPacmanActions()
    current = state.getPacmanState().configuration.direction
    if current == Directions.STOP: current = Directions.NORTH
    left = Directions.LEFT[current]
    if left in legal: return left
    if current in legal: return current
    if Directions.RIGHT[current] in legal: return Directions.RIGHT[current]
    if Directions.LEFT[left] in legal: return Directions.LEFT[left]
    return Directions.STOP

class MeuAgente(Agent):     
  def getPacmanSuccessors(self, legalActions, state):
    return [(state.generateSuccessor(self.index, action), action, state.generateSuccessor(self.index, action).getPacmanPosition()) for action in legalActions]

  def getAction(self, state):
    from util import PriorityQueue, Counter, manhattanDistance
    
    #extrai posicao das comidas para que o pacman possa se orientar
    gridComidas = state.getFood()
    #transforma em lista para ser utilizada em iteracoes posteriores
    posicaoComidas = list(gridComidas.asList())
    #posicao da primeira comida que sera perseguida pelo pacman
    _, posProxComida = min([(manhattanDistance(state.getPacmanPosition(), pos)
        ,pos) for pos in posicaoComidas])
    #armazena posicoes ja percorridas, para que o a* nao fique em loop infinito
    posVisitadas = set()

    heap = PriorityQueue()
	#armazena estados sucessores ao estado inicial no heap de caminhos
    for proxEstado, proxAcao, proxPos in self.getPacmanSuccessors(
      state.getLegalActions(self.index),state):
      # heuristica eh a distancia de manhattan e o custo de um estado para um estado
      # imediatamente adjacente
      prioridade =  manhattanDistance(proxPos, posProxComida) + 1
      #coloca estados imediatamente adjacentes ao inicial no heap de caminhos
      heap.push((proxEstado, proxAcao, 1), prioridade)
      posVisitadas.add(proxPos)

    while not heap.isEmpty():
      estadoAtual, primAcao, numAcoes = heap.pop()
      if estadoAtual.getPacmanPosition() == posProxComida:
        #retorna primeira acao do caminho, pois o nelhor caminho foi achado
	return primAcao
      for proxEstado, proxAcao, proxPos in self.getPacmanSuccessors(
          estadoAtual.getLegalActions(self.index),estadoAtual):
        if not proxEstado.getPacmanPosition() in estadoAtual.getGhostPositions():
          if proxEstado.getPacmanPosition() not in posVisitadas:
            numAcoes += 1
            heuristica = manhattanDistance(proxPos, posProxComida)
            #coloca novo estado no heap para continuar montando caminho
	    heap.push((proxEstado, primAcao, numAcoes), numAcoes + heuristica)
            #marca posicao como visitada, para que o pacman nao fique em loop infinito
	    posVisitadas.add(proxPos)
    
    # retorna acao aleatoria, pois nesse ponto nao ha mais acao boa
    return random.choice(state.getLegalPacmanActions())

class GreedyAgent(Agent):
  def __init__(self, evalFn="scoreEvaluation"):
    self.evaluationFunction = util.lookup(evalFn, globals())
    assert self.evaluationFunction != None
        
  def getAction(self, state):
    # Generate candidate actions
    legal = state.getLegalPacmanActions()
    if Directions.STOP in legal: legal.remove(Directions.STOP)
      
    successors = [(state.generateSuccessor(0, action), action) for action in legal] 
    scored = [(self.evaluationFunction(state), action) for state, action in successors]
    bestScore = max(scored)[0]
    bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
    return random.choice(bestActions)
  
def scoreEvaluation(state):
  return state.getScore()  
