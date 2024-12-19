import copy
import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()

  matrix = []
  for line in lines:
    row = []
    for char in line:
      row.append(int(char)) 
    matrix.append(row)

  return matrix

def part1():
  input = read_input(10, False)
  MAX = len(input)

  score = 0
  paths = []
  for r in range(len(input)):
    for c in range(len(input[r])):
      if input[r][c] == 0:
        print(r, c)
        state = [((r, c), [])]
        peaks = []

        while len(state) > 0:
          pos, visited = state.pop()
          row, col = pos
          # Danke, Merkel
          new_visited = copy.deepcopy(visited)

          if (row, col) in new_visited:
            continue
          else:
            new_visited.append((row, col))

          if input[row][col] == 9:
            if pos not in peaks:
              score += 1
              peaks.append(pos)
              paths.append(new_visited)
            continue
          
          if row - 1 >= 0 and input[row - 1][col] == input[row][col] + 1:
            state.append(((row - 1, col), new_visited))
          if row + 1 < MAX and input[row + 1][col] == input[row][col] + 1:
            state.append(((row + 1, col), new_visited))
          if col - 1 >= 0 and input[row][col - 1] == input[row][col] + 1:
            state.append(((row, col - 1), new_visited))
          if col + 1 < MAX and input[row][col + 1] == input[row][col] + 1:
            state.append(((row, col + 1), new_visited)) 
    
  return score


def part2():
  input = read_input(10, False)
  MAX = len(input)

  score = 0
  paths = []
  for r in range(len(input)):
    for c in range(len(input[r])):
      if input[r][c] == 0:
        print(r, c)
        state = [((r, c), [])]
        peaks = []

        while len(state) > 0:
          pos, visited = state.pop()
          row, col = pos
          # Danke, Merkel
          new_visited = copy.deepcopy(visited)

          if (row, col) in new_visited:
            continue
          else:
            new_visited.append((row, col))

          if input[row][col] == 9:
            # if pos not in peaks:
            score += 1
              # peaks.append(pos)
            paths.append(new_visited)
            continue
          
          if row - 1 >= 0 and input[row - 1][col] == input[row][col] + 1:
            state.append(((row - 1, col), new_visited))
          if row + 1 < MAX and input[row + 1][col] == input[row][col] + 1:
            state.append(((row + 1, col), new_visited))
          if col - 1 >= 0 and input[row][col - 1] == input[row][col] + 1:
            state.append(((row, col - 1), new_visited))
          if col + 1 < MAX and input[row][col + 1] == input[row][col] + 1:
            state.append(((row, col + 1), new_visited)) 
    
  return score
  
  
if __name__ == '__main__':
  # print(part1())
  print(part2())
