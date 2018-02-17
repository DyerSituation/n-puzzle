import sys
import time
import math

start_time = time.clock()
searchType = sys.argv[1]
grid = sys.argv[2].split(",")

def swapPos(zeroPos, newPos, boardList):
		tempList = list(boardList)
		tempElement = tempList[zeroPos]
		tempList[zeroPos] = tempList[newPos]
		tempList[newPos] = tempElement
		return tempList
	
def moveList(boardList, zeroPos):
	#given list, produce list of acceptible lists
	rowLen = int(math.sqrt(len(boardList)))
	column = int(zeroPos % rowLen)
	boards = []
	#up
	if(zeroPos > rowLen - 1):
		newPos = zeroPos - rowLen
		boards.append(swapPos(zeroPos, newPos, boardList))
	#down
	if(zeroPos < len(boardList) - 1):
		newPos = zeroPos + rowLen
		boards.append(swapPos(zeroPos, newPos, boardList))
	#left
	if(column > 0):
		newPos = zeroPos - 1
		boards.append(swapPos(zeroPos, newPos, boardList))
	#right
	if(column < rowLen - 1):
		newPos = zeroPos + 1
		boards.append(swapPos(zeroPos, newPos, boardList))
	return boards

class BoardState:
	pathList = []
	pathCost = 0
	addX = 0

	def __init__(self, boardList):
		self.parent = None
		self.child = boardList
		
class nodeQueue:
	queue = []
	elements = set([])
	def add(self, x):
		self.queue.append(x)
		self.elements.add(x)
		
	def remove(self):
		self.elements.discard(0)
		return self.queue.pop(0)
		
class solver:
	ds = []

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