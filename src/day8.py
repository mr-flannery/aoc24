import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()

  index = {}
  for row in range(len(lines)):
    for col in range(len(lines[row])):
      if lines[row][col] == '.':
        continue
      if lines[row][col] not in index:
        index[lines[row][col]] = []
      index[lines[row][col]].append((row, col))
  
  return lines, index

def part1():
  input = read_input(8, False)
  lines, index = input

  antinodes = set()
  for _, values in index.items():
    for i in range(0, len(values)):
      for j in range(i+1, len(values)):
        row_dist = values[i][0] - values[j][0]
        col_dist = values[i][1] - values[j][1]
        anitnode1 = (values[i][0] + row_dist, values[i][1] + col_dist)
        antinode2 = (values[j][0] - row_dist, values[j][1] - col_dist)
        if anitnode1[0] >= 0 and anitnode1[0] < len(lines) and anitnode1[1] >= 0 and anitnode1[1] < len(lines[0]):
          antinodes.add(anitnode1)
        if antinode2[0] >= 0 and antinode2[0] < len(lines) and antinode2[1] >= 0 and antinode2[1] < len(lines[0]):
          antinodes.add(antinode2)

  return len(antinodes)

def part2():
  input = read_input(8, False)
  lines, index = input

  antinodes = set()
  for _, values in index.items():
    for i in range(0, len(values)):
      for j in range(i+1, len(values)):
        row_dist = values[i][0] - values[j][0]
        col_dist = values[i][1] - values[j][1]
        
        antinode1 = (values[i][0], values[i][1])
        
        while antinode1[0] >= 0 and antinode1[0] < len(lines) and antinode1[1] >= 0 and antinode1[1] < len(lines[0]):
          antinodes.add(antinode1)
          antinode1 = (antinode1[0] + row_dist, antinode1[1] + col_dist)

        antinode2 = (values[j][0], values[j][1])
        while antinode2[0] >= 0 and antinode2[0] < len(lines) and antinode2[1] >= 0 and antinode2[1] < len(lines[0]):
          antinodes.add(antinode2)
          antinode2 = (antinode2[0] - row_dist, antinode2[1] - col_dist)

  return len(antinodes)


if __name__ == '__main__':
  # print(part1())
  print(part2())
