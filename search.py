# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  
  #print "Start:", problem.getStartState()
  #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  #print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
  pilha = util.Stack()
  estadoAtual = problem.getStartState()
  pilha.push(estadoAtual)
  while(not problem.isGoalState(estadoAtual)):
    for estado in problem.getSuccessors():
      pilha.push(estado)
    if pilha.isEmpty():
        break
    estado = pilha.pop()
  
  return util.raiseNotDefined()
    
  

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  from util import PriorityQueue


  def retornaListaSequenciaAcoes(infoEstadoFinal):
    
    def preencheListaAcoes(infoEstadoFinal, listaAcoes):
      if infoEstadoFinal.pai is not None:
        preencheListaAcoes(infoEstadoFinal.infoEstadoPai, listaAcoes)
      listaAcoes.append(infoEstadoFinal.direcao)

    listaAcoes = []
    preencheListaAcoes(infoEstadoFinal, listaAcoes)
    return listaAcoes

  estadoAtual = problem.getStartState()
  heap = PriorityQueue()
  InfoEstado = namedtuple('InfoEstado','estado infoEstadoPai direcao profundidade')
  heap.push(InfoEstado(estadoAtual, None, None, 0),0)
  expandidos = set()
  while not heap.isEmpty():
    infoEstadoAtual = heap.pop()
    if problem.isGoalState(infoEstadoAtual.estado):
      listaAcoes = retornaListaSequenciaAcoes(infoEstadoAtual) 
      #retorna a partir do 1 pois o 0 é o estado inicial
      return lista[1:]
    expandidos.add(infoEstadoAtual)
    for estado in problem.getSuccessors(infoEstadoAtual.estado):
      infoSucessor = InfoEstado(estado[0], infoEstadoAtual, estado[1]
          ,infoEstadoAtual.profundidade + 1)
      if infoSucessor not in expandidos:
        prioridade = infoEstadoAtual.profundidade + heuristic(
            infoSucessor.estado, problem)
        heap.push(infoSucessor,prioridade)
     
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
