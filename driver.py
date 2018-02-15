import sys
import time

start_time = time.clock()
searchType = sys.argv[1]
grid = sys.argv[2]
print searchType
print grid
for i in range (0,100000):
	print " "
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

