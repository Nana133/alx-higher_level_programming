#!/usr/bin/python3
"""Print alphabet in reverse order alterning upper and lower case"""

g = 0
for c in range(ord('z'), ord('a') - 1, -1):
print("{}".format(chr(c - g)), end="")
g = 32 if g == 0 else 0
