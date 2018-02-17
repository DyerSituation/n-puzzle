import sys
import time
import math

start_time = time.clock()
searchType = sys.argv[1]
grid = sys.argv[2].split(",")
rowLen = int(math.sqrt(len(grid)))



class BoardState:
	pathList = []
	pathCost = 0
	addX = 0

	def __init__(self, boardList):
		self.parent = None
		self.child = boardList
		self.ID = ''.join(boardList)
		self.zeroPos = boardList.index(0)
		
class nodeQueue:
	queue = []
	elements = set([])
	def add(self, x):
		self.queue.append(x)
		self.elements.add(x)
		
	def remove(self):
		self.elements.discard(0)
		return self.queue.pop(0)
	
	def isEmpty(self):
		return len(self.queue) < 1
		
class solver:
	
	def swapPos(self, zeroPos, newPos, state):
		tempList = list(state.child)
		tempElement = tempList[zeroPos]
		tempList[zeroPos] = tempList[newPos]
		tempList[newPos] = tempElement
		state2 = BoardState(tempList)
		state.zeroPos = newPos
		return state2
	
	def moveList(self, state, zeroPos):
		#given list, produce list of acceptible lists
		boardList = state.child
		column = int(zeroPos % rowLen)
		states = []
		#up
		if(zeroPos > rowLen - 1):
			newPos = zeroPos - rowLen
			states.append(self.swapPos(zeroPos, newPos, state))
		#down
		if(zeroPos < len(boardList) - 1):
			newPos = zeroPos + rowLen
			states.append(self.swapPos(zeroPos, newPos, state))
		#left
		if(column > 0):
			newPos = zeroPos - 1
			states.append(self.swapPos(zeroPos, newPos, state))
		#right
		if(column < rowLen - 1):
			newPos = zeroPos + 1
			states.append(self.swapPos(zeroPos, newPos, state))
		return states
	
	def main(self):
		frontier = nodeQueue()
		explored = set([])
		while not frontier.isEmpty():
			state = frontier.remove()
			explored.add(state)
			
			if self.goalTest(state):
				return self.success(State)
				
			children = self.moveList(state[0], state[1]) # board and 0 position
			for child in children:
				if child not in frontier:
					if child not in explored:
						frontier.add(child)
		return fail()
	
def main():
	print ("searchtype: ", searchType)
	firstState = BoardState(grid)
		
	boardList = moveList(grid, 1)
	for board in boardList:
		for i in range (0,9):
			print(board[i]),
			if((i + 1) % 3 == 0):
				print "\n"
		print "\n done \n"

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