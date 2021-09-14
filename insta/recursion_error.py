import sys

def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n-1, sum+n)
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)