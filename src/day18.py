import copy
from functools import cache
from itertools import chain
import re
from queue import PriorityQueue

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()

  coords = []
  for line in lines:
    x,y = re.findall(r'(\d+)', line)
    coords.append((int(x), int(y)))

  return coords


def run(input, grid_size):
  grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
  
  for x, y in input:
    grid[y][x] = '#'
  
  # [print(''.join(row)) for row in grid]

  def dijkstra(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = PriorityQueue()
    pq.put((0, 0, 0))  # (cost, x, y)
    visited = set()
    costs = {}
    
    while not pq.empty():
      cost, x, y = pq.get()
      if (x, y) in visited:
        continue
      visited.add((x, y))
      
      if (x,y) not in costs:
        costs[(x,y)] = cost
      else:
        costs[(x,y)] = min(costs[(x,y)], cost)
      
      for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[ny][nx] == '.':
          pq.put((cost + 1, nx, ny))
    
    if (len(grid)-1,len(grid)-1) not in costs:
      return -1
    else:
      return costs[(len(grid)-1,len(grid)-1)]
  
  shortest_path_cost = dijkstra(grid)
  return shortest_path_cost

def part1():
  input = read_input(18, False)
  
  return run(input[:1024], 71)

def part2():
  input = read_input(18, False)

  def binary_search(input):
    low, high = 0, len(input)
    while low < high:
      mid = (low + high) // 2
      if run(input[:mid], 71) == -1:
        high = mid
      else:
        low = mid + 1
    return low

  first_invalid_index = binary_search(input)
  return first_invalid_index - 1 # technically, the binary search returns the first invalid cutoff, i.e. the index we're looking for is one less, since the cutoff is exclusive

if __name__ == '__main__':
  # print(part1())
  print(part2())
