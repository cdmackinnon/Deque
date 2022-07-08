import timeit
from unittest import case
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)

  if n>= 1:
    Hanoi_rec(n-1, s, d, a)
    d.push(s.pop())
    Hanoi_rec(n-1, a, s, d)
  else:
    d.push(s.pop())
  print(n, s, a, d)
  print()
  return

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=3
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")