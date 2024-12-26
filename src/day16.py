import copy
from functools import cache
from itertools import chain
import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()


  maze = [list(line) for line in lines]
  return maze

def move(maze, row, col, visited, score, direction):
  if maze[row][col] == 'E':
    return score

  if (row, col) in visited:
    return 999_999_999_999_999
  
  visited.add((row, col))

  match direction:
    case 'N':
      next_scores = []
      if maze[row-1][col] == '.':
        next_scores.append(move(maze, row-1, col, visited, score, 'N'))
      if maze[row][col-1] == '.':
        next_scores.append(move(maze, row, col-1, visited, score, 'W')+1000)
      if maze[row][col+1] == '.':
        next_scores.append(move(maze, row, col+1, visited, score, 'E')+1000)
      if next_scores:
        return min(next_scores)
      else:
        return 999_999_999_999_999
    case 'S':
      next_scores = []
      if maze[row+1][col] == '.':
        next_scores.append(move(maze, row+1, col, visited, score, 'S'))
      if maze[row][col-1] == '.':
        next_scores.append(move(maze, row, col-1, visited, score, 'W')+1000)
      if maze[row][col+1] == '.':
        next_scores.append(move(maze, row, col+1, visited, score, 'E')+1000)
      if next_scores:
        return min(next_scores)
      else:
        return 999_999_999_999_999
    case 'E': 
      next_scores = []
      if maze[row][col+1] == '.':
        next_scores.append(move(maze, row, col+1, visited, score, 'E'))
      if maze[row-1][col] == '.':
        next_scores.append(move(maze, row-1, col, visited, score, 'N')+1000)
      if maze[row+1][col] == '.':
        next_scores.append(move(maze, row+1, col, visited, score, 'S')+1000)
      if next_scores:
        return min(next_scores)
      else:
        return 999_999_999_999_999
    case 'W':
      next_scores = []
      if maze[row][col-1] == '.':
        next_scores.append(move(maze, row, col-1, visited, score, 'W'))
      if maze[row-1][col] == '.':
        next_scores.append(move(maze, row-1, col, visited, score, 'N')+1000)
      if maze[row+1][col] == '.':
        next_scores.append(move(maze, row+1, col, visited, score, 'S')+1000)
      if next_scores:
        return min(next_scores)
      else:
        return 999_999_999_999_999

  
def part1():
  input = read_input(16, True)

  current_row, current_col = None, None
  for row in range(len(input)):
    for col in range(len(input[row])):
      if input[row][col] == 'S':
        current_col = col
        current_row = row

  return move(input, current_row, current_col, set(), 0, 'E')
  

def part2():
  input = read_input(16, True)
  
      



if __name__ == '__main__':
  print(part1())
  # print(part2())
