import sys
import time
import math
import heapq

start_time = time.clock()
searchType = sys.argv[1]
grid = sys.argv[2].split(",")
rowLen = int(math.sqrt(len(grid)))
elementCount = len(grid)
correctString = ''
for i in range (0, elementCount):
	correctString += `i`



class BoardState:
	pathCost = 0
	def __init__(self, boardList):
		self.parent = None
		self.direction = None
		self.child = boardList
		self.ID = ''.join(boardList)
		self.zeroPos = boardList.index("0")

class nodeHeap:
	goal = []
	for i in range (0, elementCount):
		goal.append(i)
		
	heap = []
	elements = set([])
	
	def findDistance(self, state):
		distance = 0
		for i in range (0, elementCount):
			distance += abs(self.goal[i] - int(state.child[i]))
		return distance
	
	def add(self, x):
		fn = self.findDistance(x) + x.pathCost
		directionBonus = 0
		if x.direction == None:
			directionBonus = 0
		elif x.direction == "up":
			directionBonus = 1
		elif x.direction == "down":
			directionBonus = 2
		elif x.direction == "left":
			directionBonus = 3
		elif x.direction == "right":
			directionBonus = 4
		heapq.heappush(self.heap, (fn*10 + directionBonus, x))
		self.elements.add(x.ID)
	def remove(self):
		item = heapq.heappop(self.heap)
		self.elements.discard(item[1].ID)
		return item[1]
		
	def isEmpty(self):
		return len(self.heap) < 1
	
class nodeQueue:
	queue = []
	elements = set([])
	def add(self, x):
		self.queue.append(x)
		self.elements.add(x.ID)
		
	def remove(self):
		item = self.queue.pop(0)
		self.elements.discard(item.ID)
		return item
	
	def isEmpty(self):
		return len(self.queue) < 1
		
class nodeStack:
	stack = []
	elements = set([])
	def add(self, x):
		self.stack.append(x)
		self.elements.add(x.ID)
		
	def remove(self):
		item = self.stack.pop()
		self.elements.discard(item.ID)
		return item
	
	def isEmpty(self):
		return len(self.stack) < 1
		
		

class Solver:
	
	def printState(self, state):
		board = state.child
		print "board start"
		for i in range (0, len(board)):
			print(board[i]),
			if((i + 1) % 3 == 0):
				print "\n"
		print "board end"
	
	def swapPos(self, zeroPos, newPos, state, direction):
		tempList = list(state.child)
		tempElement = tempList[zeroPos]
		tempList[zeroPos] = tempList[newPos]
		tempList[newPos] = tempElement
		state2 = BoardState(tempList)
		state2.zeroPos = newPos
		state2.parent = state
		state2.direction = direction
		state2.pathCost = state.pathCost + 1
		return state2
	
	def moveList(self, state):
		#given list, produce list of acceptible lists
		boardList = state.child
		zeroPos = state.zeroPos
		column = int(zeroPos % rowLen)
		states = []
		#up
		if(zeroPos > rowLen - 1):
			newPos = zeroPos - rowLen
			states.append(self.swapPos(zeroPos, newPos, state, "up"))
		#down
		if(zeroPos < len(boardList) - rowLen):
			newPos = zeroPos + rowLen
			states.append(self.swapPos(zeroPos, newPos, state, "down"))
		#left
		if(column > 0):
			newPos = zeroPos - 1
			states.append(self.swapPos(zeroPos, newPos, state, "left"))
		#right
		if(column < rowLen - 1):
			newPos = zeroPos + 1
			states.append(self.swapPos(zeroPos, newPos, state, "right"))
		if searchType == "dfs":
			return reversed(states)
		else:
			return states
	
	def main(self):
		if searchType == "bfs":
			frontier = nodeQueue()
		elif searchType == "dfs":
			frontier = nodeStack()
		else:
			frontier = nodeHeap()
		frontierSet = set([])
		initState = BoardState(grid)
		frontier.add(initState)
		frontierSet.add(initState.ID)
		explored = set([])
		path = []
		maxCost = 0
		expandCount = 0
		while not frontier.isEmpty():
			state = frontier.remove()
			frontierSet.remove(state.ID)
			explored.add(state.ID)
			# self.printState(state)
			if state.ID == correctString:
				cost_of_path = state.pathCost
				nodes_expanded = expandCount
				search_depth = state.pathCost
				max_search_depth = maxCost
				directions = []
				while state.parent is not None:
					directions.insert(0,state.direction)
					state = state.parent
				print ("path_to_goal: ", directions)
				print("cost_of_path: ", cost_of_path)
				print("nodes_expanded: ", nodes_expanded)
				print("search_depth: ", search_depth)
				print("max_search_depth ", max_search_depth)
				return 1
				
			children = self.moveList(state) # board and 0 position
			expandCount += 1
			if state.pathCost + 1 > maxCost:
				maxCost = state.pathCost + 1
			for child in children:
				if child.ID not in frontier.elements:
					if child.ID not in explored:
						frontier.add(child)
						frontierSet.add(child.ID)
		return 0
	
def main():
	firstState = BoardState(grid)
	s = Solver()
	s.main()
	
if __name__ == "__main__":
	main()
	print ("running_time: ", time.clock() - start_time)
	if sys.platform == "win32":
		import psutil
		print("max_ram_usage: ", psutil.Process().memory_info().rss)
	else:
	# Note: if you execute Python from cygwin,
	# the sys.platform is "cygwin"
	# the grading system's sys.platform is "linux2"
		import resource
		print("max_ram_usage: ", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)