import copy
from functools import cache
from itertools import chain
import re
from queue import PriorityQueue

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()


  maze = [list(line) for line in lines]
  return maze
  
def part1():
  input = read_input(16, False)

  current_row, current_col = None, None
  exit_row, exit_col = None, None
  for row in range(len(input)):
    for col in range(len(input[row])):
      if input[row][col] == 'S':
        current_col = col
        current_row = row
      if input[row][col] == 'E':
        exit_col = col
        exit_row = row
        input[row][col] = '.'

  queue = [(current_row, current_col, 0, 'E', set())]

  results = []

  while queue:
    row, col, score, direction, visited = queue.pop(0)
    
    if (row, col) == (exit_row, exit_col):
      results.append(score)

    if (row, col) in visited:
      continue

    if results and score >= min(results):
      continue
    
    visited.add((row, col))

    match direction:
      case 'N':
        if input[row-1][col] == '.':
          queue.append((row-1, col, score + 1, 'N', copy.deepcopy(visited)))
        if input[row][col-1] == '.':
          queue.append((row, col-1, score + 1001, 'W', copy.deepcopy(visited)))
        if input[row][col+1] == '.':
          queue.append((row, col+1, score + 1001, 'E', copy.deepcopy(visited)))
      case 'S':
        if input[row+1][col] == '.':
          queue.append((row+1, col, score + 1, 'S', copy.deepcopy(visited)))
        if input[row][col-1] == '.':
          queue.append((row, col-1, score + 1001, 'W', copy.deepcopy(visited)))
        if input[row][col+1] == '.':
          queue.append((row, col+1, score + 1001, 'E', copy.deepcopy(visited)))
      case 'E': 
        if input[row][col+1] == '.':
          queue.append((row, col+1, score + 1, 'E', copy.deepcopy(visited)))
        if input[row-1][col] == '.':
          queue.append((row-1, col, score + 1001, 'N', copy.deepcopy(visited)))
        if input[row+1][col] == '.':
          queue.append((row+1, col, score + 1001, 'S', copy.deepcopy(visited)))
      case 'W':
        if input[row][col-1] == '.':
          queue.append((row, col-1, score + 1, 'W', copy.deepcopy(visited)))
        if input[row-1][col] == '.':
          queue.append((row-1, col, score + 1001, 'N', copy.deepcopy(visited)))
        if input[row+1][col] == '.':
          queue.append((row+1, col, score + 1001, 'S', copy.deepcopy(visited)))

  return min(results)
  

def part2():
  input = read_input(16, True)
  
      



if __name__ == '__main__':
  print(part1())
  # print(part2())
