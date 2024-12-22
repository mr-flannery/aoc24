import copy
from functools import cache
import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()

  robots = []
  for line in lines:
    robots.append(list(map(int, re.findall(r'(\-?\d+)', line))))

  return robots


def part1():
  input = read_input(14, False)
  x_max = 101
  y_max = 103

  quadrants = { 1:0, 2:0, 3:0, 4:0 }

  for robot in input:
    x,y,dx,dy = robot
    final_x = (x + 100*dx) % x_max
    final_y = (y + (100*dy)) % y_max

    if final_x < x_max//2 and final_y < y_max//2:
      quadrants[1] += 1
    elif final_x > x_max//2 and final_y < y_max//2:
      quadrants[2] += 1
    elif final_x < x_max//2 and final_y > y_max//2:
      quadrants[3] += 1
    elif final_x > x_max//2 and final_y > y_max//2:
      quadrants[4] += 1

  return quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]


def part2():
  input = read_input(14, False)
  x_max = 101
  y_max = 103

  i = 1
  while True:
    field = [['.' for _ in range(x_max)] for _ in range(y_max)]
    for robot in input:
      x,y,dx,dy = robot
      robot[0] = (x + dx) % x_max
      robot[1] = (y + dy) % y_max
      field[robot[1]][robot[0]] = '#'
    
    check_str = '###############################'
    for row in field:
      for col in range(len(row) - len(check_str)):
        if check_str in ''.join(row):
          for row in field:
            print(''.join(row))
          print()
          return i
    i += 1
      



if __name__ == '__main__':
  # print(part1())
  print(part2())
