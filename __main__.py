from engine import test_alternatives
from functools import reduce
import numpy as np

class Node: 
  def __init__(self, value, left, right): 
    self.value = value 
    self.left = left 
    self.right = right

def alternative_binary_tree(arr: list[int]):...

def alternative_while_loop(arr: list[int]):
  total = 0
  i = 0
  while i < len(arr):
    total += arr[i]
    i += 1
  return total

def alternative_for(arr: list[int]):
  result = 0
  for x in arr:
    result += x

def alternative_sum(arr: list[int]):
  sum(arr) 

def alternative_reduce(arr: list[int]):
  reduce(lambda x, y: x + y, arr)

def alternative_list_comprehension(arr: list[int]):
  sum([x for x in arr])

def alternative_numpy_sum(arr: list[int]):
  np.sum(arr)

def main(): 
  report, best_alternative = test_alternatives(
    alternatives=[
      alternative_for, 
      alternative_sum, 
      alternative_reduce, 
      alternative_numpy_sum,
      alternative_list_comprehension,
      alternative_while_loop
    ], 
    ranges=[
      1000000, # 1 milhão 
      2000000,
      3000000,
      4000000,
      5000000,
      6000000,
      7000000,
      8000000,
      9000000,
    ]
  )

  print(report)
  print(f"a função mais performatica é: {best_alternative}")

if __name__ == "__main__":
  main()
