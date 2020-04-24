import sys
sys.path.append('/lru_cache.py')
from lru_cache import LRUCache

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

cache = LRUCache(10000)

for something in range(len(names_1)):
    cache.set(names_1[something], names_1[something])
    
# Replace the nested for loops below with your improvements
for y in names_2:
    if cache.get(y) == y:
        duplicates.append(y)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
