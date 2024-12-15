import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.readlines()

  for row in range(len(lines)):
    lines[row] = lines[row].strip()
  for row in range(len(lines)):
    for col in range(len(lines[row])):
      if lines[row][col] == '^':
        return lines, row, col
  

def part1():
  map, current_row, current_col = read_input(6, False)
  visited = set()
  direction = 'up'

  while True:
    visited.add((current_row, current_col))
    if direction == 'up':
      if current_row == 0:
        break
      elif map[current_row - 1][current_col] == '#':
        direction = 'right'
      else:
        current_row -= 1
    elif direction == 'right':
      if current_col == len(map[0]) - 1:
        break
      elif map[current_row][current_col + 1] == '#':
        direction = 'down'
      else:
        current_col += 1
    elif direction == 'down':
      if current_row == len(map) - 1:
        break
      elif map[current_row + 1][current_col] == '#':
        direction = 'left'
      else:
        current_row += 1
    elif direction == 'left':
      if current_col == 0:
        break
      elif map[current_row][current_col - 1] == '#':
        direction = 'up'
      else:
        current_col -= 1
    
  return len(visited)  
  
def part2():
  map, start_row, start_col = read_input(6, False)

  possible_loops = 0
  for row in range(len(map)):
    for col in range(len(map[row])):
      current_row, current_col = start_row, start_col
      if map[row][col] == '.':
        map[row] = map[row][:col] + '#' + map[row][col+1:]
        
        visited = set()
        direction = 'up'

        while True:
          if (current_row, current_col, direction) in visited:
            possible_loops += 1
            break
          visited.add((current_row, current_col, direction))
          if direction == 'up':
            if current_row == 0:
              break
            elif map[current_row - 1][current_col] == '#':
              direction = 'right'
            else:
              current_row -= 1
          elif direction == 'right':
            if current_col == len(map[0]) - 1:
              break
            elif map[current_row][current_col + 1] == '#':
              direction = 'down'
            else:
              current_col += 1
          elif direction == 'down':
            if current_row == len(map) - 1:
              break
            elif map[current_row + 1][current_col] == '#':
              direction = 'left'
            else:
              current_row += 1
          elif direction == 'left':
            if current_col == 0:
              break
            elif map[current_row][current_col - 1] == '#':
              direction = 'up'
            else:
              current_col -= 1

        map[row] = map[row][:col] + '.' + map[row][col+1:]
  
  return possible_loops


if __name__ == '__main__':
  # print(part1())
  print(part2())
