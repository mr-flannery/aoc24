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

def run_game(x,y, a_x, a_y, b_x, b_y):
  x_temp = x
  y_temp = y
  a_counter = 0
  b_counter = 0
  while True:
    if x_temp % b_x == 0 and y_temp % b_y == 0 and x_temp // b_x == y_temp // b_y:
      b_counter += x_temp // b_x
      return a_counter, b_counter
    if x_temp == 0 and y_temp == 0:
      return a_counter, b_counter
    if x_temp < 0 or y_temp < 0:
      return None, None
    x_temp -= a_x
    y_temp -= a_y
    a_counter += 1

# lol nvm, this approach does not scale for part2
def solve(game):
  a_x, a_y, b_x, b_y, x, y = game

  # part 2
  x += 10000000000000
  y += 10000000000000

  a1_counter, b1_counter = run_game(x, y, a_x, a_y, b_x, b_y)
  b2_counter, a2_counter = run_game(x, y, b_x, b_y, a_x, a_y)

  # part 1
  # if a1_counter is not None and (a1_counter > 100 or b1_counter > 100):
  #   a1_counter, b1_counter = None, None
  # if a2_counter is not None and (a2_counter > 100 or b2_counter > 100):
  #   a2_counter, b2_counter = None, None

  if a1_counter is None and a2_counter is None:
    return 0
  elif a1_counter is None:
    return 3*a2_counter+b2_counter
  elif a2_counter is None:
    return 3*a1_counter+b1_counter
  else:
    return min(3*a1_counter+b1_counter, 3*a2_counter+b2_counter)
  

def part1():
  input = read_input(13, False)

  total_tokens = 0

  for i in range(len(input)):
    game = input[i]
    # total_tokens += solve(game)
    solved = False
    tokens = 999999999
    a_x, a_y, b_x, b_y, x, y = game
    for a in range(101):
      for b in range(101):
        if a_x*a + b_x*b == x and a_y*a + b_y*b == y:
          tokens = min(tokens, 3*a+b)
          solved = True
    if solved:
      # print(i)
      total_tokens += tokens
  
  return total_tokens

def part2():
  input = read_input(13, False)

  total_tokens = 0

  for i in range(len(input)):
    print(i)
    game = input[i]
    result =  solve(game)
    total_tokens += result
  
  return total_tokens

if __name__ == '__main__':
  # print(part1())
  print(part2())
