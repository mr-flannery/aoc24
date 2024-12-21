import copy
from functools import cache
import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()

  matrix = []
  for line in lines:
    row = []
    for char in line:
      row.append(char) 
    matrix.append(row)

  return matrix

def part1():
  input = read_input(12, False)
  MAX = len(input)

  visited = set()
  regions = []
  result = 0

  for row in range(len(input)):
    for col in range(len(input[row])):
      if (row, col) not in visited:
        # flood fill region
        region = set()
        perimeter = 0
        queue = [(row, col)]
        while queue:
          r, c = queue.pop()
          if (r, c) in visited:
            continue
          visited.add((r, c))
          region.add((r, c))

          if r == 0:
            perimeter += 1
          if c == 0:
            perimeter += 1
          if r == MAX - 1:
            perimeter += 1
          if c == MAX - 1:
            perimeter += 1
          
          if r - 1 >= 0:
            if input[r - 1][c] == input[r][c]:
              if (r - 1, c) not in region:
                queue.append((r - 1, c))
            else:
              perimeter += 1
          if c - 1 >= 0:
            if input[r][c - 1] == input[r][c]:
              if (r, c - 1) not in region:
                queue.append((r, c - 1))
            else:
              perimeter += 1
          if r + 1 < MAX:
            if input[r + 1][c] == input[r][c]:
              if (r + 1, c) not in region:
                queue.append((r + 1, c))
            else:
              perimeter += 1
          if c + 1 < MAX:
            if input[r][c + 1] == input[r][c]:
              if (r, c + 1) not in region:
                queue.append((r, c + 1))
            else:
              perimeter += 1
        regions.append((region, perimeter))
        result += len(region) * perimeter

  return result
          
      


if __name__ == '__main__':
  print(part1())
  # print(part2())

