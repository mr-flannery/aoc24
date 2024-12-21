import copy
from functools import cache
import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().split('\n\n')

  games = []
  for line in lines:
    games.append(list(map(int, re.findall(r'\d+', line))))

  return games

def part1():
  input = read_input(13, False)

  total_tokens = 0

  for game in input:
    a_x, a_y, b_x, b_y, x, y = game

    a_cost = (a_x**2 + a_y**2)**(1/2)
    b_cost = (b_x**2 + b_y**2)**(1/2)
    if a_cost > b_cost:
      x_temp = x
      y_temp = y
      a_counter = 0
      b_counter = 0
      if x % b_x == 0 and y % b_y == 0:
        b_counter += x // b_x
        total_tokens += b_counter * 3
        print(f"reached {x}/{y} with {a_counter} steps of {a_x}/{a_y} and {b_counter} steps of {b_x}/{b_y}, at cost of {a_counter * 3 + b_counter}")
        continue
      while True:
        if x_temp % b_x == 0 and y_temp % b_y == 0:
          b_counter += x_temp // b_x
          total_tokens += a_counter * 3 + b_counter
          print(f"reached {x}/{y} with {a_counter} steps of {a_x}/{a_y} and {b_counter} steps of {b_x}/{b_y}, at cost of {a_counter * 3 + b_counter}")
          break
        if x_temp == 0 and y_temp == 0:
          total_tokens += a_counter * 3 + b_counter
          print(f"reached {x}/{y} with {a_counter} steps of {a_x}/{a_y} and {b_counter} steps of {b_x}/{b_y}, at cost of {a_counter * 3 + b_counter}")
          break
        if x_temp < 0 or y_temp < 0:
          break
        x_temp -= a_x
        y_temp -= a_y
        a_counter += 1
    else:
      x_temp = x
      y_temp = y
      a_counter = 0
      b_counter = 0
      if x % a_x == 0 and y % a_y == 0:
        a_counter += x // a_x
        total_tokens += a_counter * 3
        print(f"reached {x}/{y} with {a_counter} steps of {a_x}/{a_y} and {b_counter} steps of {b_x}/{b_y}, at cost of {a_counter * 3 + b_counter}")
        continue
      while True:
        if x_temp % a_x == 0 and y_temp % a_y == 0:
          a_counter += x_temp // a_x
          total_tokens += a_counter * 3 + b_counter
          print(f"reached {x}/{y} with {a_counter} steps of {a_x}/{a_y} and {b_counter} steps of {b_x}/{b_y}, at cost of {a_counter * 3 + b_counter}")
          break
        if x_temp == 0 and y_temp == 0:
          total_tokens += a_counter * 3 + b_counter
          print(f"reached {x}/{y} with {a_counter} steps of {a_x}/{a_y} and {b_counter} steps of {b_x}/{b_y}, at cost of {a_counter * 3 + b_counter}")
          break
        if x_temp < 0 or y_temp < 0:
          break
        x_temp -= b_x
        y_temp -= b_y
        b_counter += 1
      
  
  return total_tokens

if __name__ == '__main__':
  print(part1())
  # print(part2())
