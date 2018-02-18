import sys
import time
import math

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
			return -1
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
			
			#need to change
			if state.ID == correctString:
				print "A winner is you!"
				print("path cost ", state.pathCost)
				print("max cost ", maxCost)
				print("expand Count ", expandCount)
				directions = []
				while state is not None:
					print(state.ID)
					directions.insert(0,state.direction)
					state = state.parent
				print directions

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
						
		print "Nice try"
		return 0
	
def main():
	print ("searchtype: ", searchType)
	firstState = BoardState(grid)

	s = Solver()
	print correctString
	s.main()
		
	# boardList = moveList(grid, 1)
	# for board in boardList:
	# 	for i in range (0,9):
	# 		print(board[i]),
	# 		if((i + 1) % 3 == 0):
	# 			print "\n"
	# 	print "\n done \n"

if __name__ == "__main__":
	main()
	print time.clock() - start_time
	if sys.platform == "win32":
		import psutil
		print("psutil", psutil.Process().memory_info().rss)
	else:
	# Note: if you execute Python from cygwin,
	# the sys.platform is "cygwin"
	# the grading system's sys.platform is "linux2"
		import resource
		print("resource", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)