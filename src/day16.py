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

  queue = PriorityQueue()
  queue.put((0, (current_row, current_col, 0, 'E')))

  visited = set()
  scores = {}

  while not queue.empty():
    row, col, score, direction = queue.get()[1]
    
    if (row, col) not in scores:
      scores[(row, col)] = score
    else:
      scores[(row, col)] = min(scores[(row, col)], score)
      
    if (row, col) in visited:
      continue

    visited.add((row, col))

    match direction:
      case 'N':
        if input[row-1][col] == '.':
          queue.put((score + 1, (row-1, col, score + 1, 'N')))
        if input[row][col-1] == '.':
          queue.put((score + 1000, (row, col-1, score + 1001, 'W')))
        if input[row][col+1] == '.':
          queue.put((score + 1000, (row, col+1, score + 1001, 'E')))
      case 'S':
        if input[row+1][col] == '.':
          queue.put((score + 1, (row+1, col, score + 1, 'S')))
        if input[row][col-1] == '.':
          queue.put((score + 1000, (row, col-1, score + 1001, 'W')))
        if input[row][col+1] == '.':
          queue.put((score + 1000, (row, col+1, score + 1001, 'E')))
      case 'E': 
        if input[row][col+1] == '.':
          queue.put((score + 1, (row, col+1, score + 1, 'E')))
        if input[row-1][col] == '.':
          queue.put((score + 1000, (row-1, col, score + 1001, 'N')))
        if input[row+1][col] == '.':
          queue.put((score + 1000, (row+1, col, score + 1001, 'S')))
      case 'W':
        if input[row][col-1] == '.':
          queue.put((score + 1, (row, col-1, score + 1, 'W')))
        if input[row-1][col] == '.':
          queue.put((score + 1000, (row-1, col, score + 1001, 'N')))
        if input[row+1][col] == '.':
          queue.put((score + 1000, (row+1, col, score + 1001, 'S')))

  return scores[(exit_row, exit_col)]
  

def part2():
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

  queue = PriorityQueue()
  queue.put((0, (current_row, current_col, 'E', [])))

  visited = set()
  scores = {}

  while not queue.empty():
    score, (row, col, direction, path) = queue.get()
    
    if (row, col) not in scores:
      scores[(row,col)] = {score: [path]}
    else:
      if score not in scores[(row,col)]:
        scores[(row,col)][score] = [path]
      else:
        scores[(row,col)][score].append(path)
      
    if (row, col, direction) in visited:
      continue

    visited.add((row, col, direction))

    match direction:
      case 'N':
        if input[row-1][col] == '.':
          queue.put((score + 1, (row-1, col, 'N', path + [(row, col, direction)])))
        if input[row][col-1] == '.':
          queue.put((score + 1001, (row, col-1,'W', path + [(row, col, direction)])))
        if input[row][col+1] == '.':
          queue.put((score + 1001, (row, col+1,'E', path + [(row, col, direction)])))
      case 'S':
        if input[row+1][col] == '.':
          queue.put((score + 1, (row+1, col, 'S', path + [(row, col, direction)])))
        if input[row][col-1] == '.':
          queue.put((score + 1001, (row, col-1,'W', path + [(row, col, direction)])))
        if input[row][col+1] == '.':
          queue.put((score + 1001, (row, col+1,'E', path + [(row, col, direction)])))
      case 'E': 
        if input[row][col+1] == '.':
          queue.put((score + 1, (row, col+1, 'E', path + [(row, col, direction)])))
        if input[row-1][col] == '.':
          queue.put((score + 1001, (row-1, col,'N', path + [(row, col, direction)])))
        if input[row+1][col] == '.':
          queue.put((score + 1001, (row+1, col,'S', path + [(row, col, direction)])))
      case 'W':
        if input[row][col-1] == '.':
          queue.put((score + 1, (row, col-1, 'W', path + [(row, col, direction)])))
        if input[row-1][col] == '.':
          queue.put((score + 1001, (row-1, col,'N', path + [(row, col, direction)])))
        if input[row+1][col] == '.':
          queue.put((score + 1001, (row+1, col,'S', path + [(row, col, direction)])))

  tiles = set()
  queue = [(exit_row, exit_col)]
  while queue:
    row, col = queue.pop()
    if (row, col) in tiles:
      continue
    tiles.add((row, col))
    if (row, col) != (current_row, current_col):
      eligble_paths = scores[(row,col)][min(scores[(row,col)].keys())]
      for path in eligble_paths:
        for prev_row, prev_col, prev_dir in path:
          queue.append((prev_row, prev_col))

  for (row, col) in tiles:
    input[row][col] = 'O'

  [print(''.join(row)) for row in input]
  
  return len(tiles)
  

if __name__ == '__main__':
  # print(part1())
  print(part2())
