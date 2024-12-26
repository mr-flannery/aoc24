import copy
from functools import cache
from itertools import chain
import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    warehouse, moves = f.read().split('\n\n')

  warehouse = [list(line) for line in warehouse.splitlines()]
  moves = list(moves.replace('\n',''))

  return warehouse, moves


def part1():
  input = read_input(15, False)
  warehouse, moves = input

  robot_row, robot_col = None, None
  for row in range(len(warehouse)):
    for col in range(len(warehouse[row])):
      if warehouse[row][col] == '@':
        robot_col = col
        robot_row = row

  for move in moves:
    match move:
      case '<':
        match warehouse[robot_row][robot_col - 1]:
          case '.':
            warehouse[robot_row][robot_col - 1] = '@'
            warehouse[robot_row][robot_col] = '.'
            robot_col -= 1
          case '#':
            pass
          case 'O':
            move = False
            for i in range(robot_col - 2, -1, -1):
              if warehouse[robot_row][i] == '#':
                break
              if warehouse[robot_row][i] == '.':
                warehouse[robot_row][robot_col] = '.'
                warehouse[robot_row][robot_col-1] = '@'
                for j in range(robot_col - 2, i - 1, -1):
                  warehouse[robot_row][j] = 'O'
                robot_col -= 1
                break
      case '>':
        match warehouse[robot_row][robot_col + 1]:
          case '.':
            warehouse[robot_row][robot_col + 1] = '@'
            warehouse[robot_row][robot_col] = '.'
            robot_col += 1
          case '#':
            pass
          case 'O':
            move = False
            for i in range(robot_col + 2, len(warehouse)):
              if warehouse[robot_row][i] == '#':
                break
              if warehouse[robot_row][i] == '.':
                warehouse[robot_row][robot_col] = '.'
                warehouse[robot_row][robot_col+1] = '@'
                for j in range(robot_col + 2, i + 1):
                  warehouse[robot_row][j] = 'O'
                robot_col += 1
                break
      case '^':
        match warehouse[robot_row - 1][robot_col]:
          case '.':
            warehouse[robot_row - 1][robot_col] = '@'
            warehouse[robot_row][robot_col] = '.'
            robot_row -= 1
          case '#':
            pass
          case 'O':
            move = False
            for i in range(robot_row - 2, -1, -1):
              if warehouse[i][robot_col] == '#':
                break
              if warehouse[i][robot_col] == '.':
                warehouse[robot_row][robot_col] = '.'
                warehouse[robot_row-1][robot_col] = '@'
                for j in range(robot_row - 2, i - 1, -1):
                  warehouse[j][robot_col] = 'O'
                robot_row -= 1
                break
      case 'v':
        match warehouse[robot_row + 1][robot_col]:
          case '.':
            warehouse[robot_row + 1][robot_col] = '@'
            warehouse[robot_row][robot_col] = '.'
            robot_row += 1
          case '#':
            pass
          case 'O':
            move = False
            for i in range(robot_row + 2, len(warehouse)):
              if warehouse[i][robot_col] == '#':
                break
              if warehouse[i][robot_col] == '.':
                warehouse[robot_row][robot_col] = '.'
                warehouse[robot_row+1][robot_col] = '@'
                for j in range(robot_row + 2, i + 1):
                  warehouse[j][robot_col] = 'O'
                robot_row += 1
                break
    
  print('\n'.join([''.join(row) for row in warehouse]))

  gps = 0 
  for row in range(len(warehouse)):
    for col in range(len(warehouse[row])):
      if warehouse[row][col] == 'O':
        gps += 100 * row + col
      
  return gps
  

def part2():
  input = read_input(15, True)
  
      



if __name__ == '__main__':
  print(part1())
  # print(part2())
