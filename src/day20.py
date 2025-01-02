import copy
from functools import cache, reduce
from itertools import chain
import re
from queue import PriorityQueue

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()

  return [list(line) for line in lines]

def find_coordinates(grid, char):
  for r, row in enumerate(grid):
    for c, val in enumerate(row):
      if val == char:
        return (r, c)
  return None

def dijkstra(grid, start, end):
  rows, cols = len(grid), len(grid[0])
  pq = PriorityQueue()
  pq.put((0, start))
  distances = {start: 0}
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  visited = set()

  while not pq.empty():
    current_distance, current_node = pq.get()

    if current_node in visited:
      continue
    visited.add(current_node)

    for direction in directions:
      neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])
      if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == '.':
        distance = current_distance + 1
        if neighbor not in distances or distance < distances[neighbor]:
          distances[neighbor] = distance
          pq.put((distance, neighbor))

  return distances

def part1():
  input = read_input(20, False)
  start = find_coordinates(input, 'S')
  end = find_coordinates(input, 'E')
  input[start[0]][start[1]] = '.'
  input[end[0]][end[1]] = '.'
  original_maze_length = dijkstra(input, start, end)[end]
  print(f"Shortest path from S to E: {original_maze_length}")

  rows, cols = len(input), len(input[0])
  shortest_paths = []

  for r in range(rows):
    for c in range(cols):
      if input[r][c] == '#':
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        path_neighbors = sum(1 for nr, nc in neighbors if 0 <= nr < rows and 0 <= nc < cols and input[nr][nc] == '.')
        if path_neighbors >= 2:
          modified_grid = copy.deepcopy(input)
          modified_grid[r][c] = '.'
          shortest_path = dijkstra(modified_grid, start, end)
          shortest_paths.append(shortest_path)

  histogram = {}
  for shortcut in shortest_paths:
    time_saved = original_maze_length - shortcut
    if time_saved not in histogram:
      histogram[time_saved] = 1
    else:
      histogram[time_saved] += 1
  
  return reduce(lambda x,y: x + y[1] if y[0] >= 100 else x, histogram.items(), 0)


def part2():
  input = read_input(20, False)
  start = find_coordinates(input, 'S')
  end = find_coordinates(input, 'E')
  input[start[0]][start[1]] = '.'
  input[end[0]][end[1]] = '.'
  original_maze_length = dijkstra(input, start, end)
  total_path_length = original_maze_length[end]
  print(f"Shortest path from S to E: {total_path_length}")

  rows, cols = len(input), len(input[0])
  points = [(r, c) for r in range(rows) for c in range(cols) if input[r][c] == '.']
  counter = 0

  # too high
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      p1, p2 = points[i], points[j]
      manhattan_distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
      if manhattan_distance <= 20:
        if abs((total_path_length - original_maze_length[p1]) - (total_path_length - original_maze_length[p2])) - manhattan_distance >= 100:
          counter += 1

  return counter

if __name__ == '__main__':
  # print(part1())
  print(part2())
