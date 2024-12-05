import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = list(map(lambda s: str.strip(s), f.readlines()))

  return lines

def tilt_left(matrix):
  num_cols = len(matrix[0])
  num_rows = len(matrix)
  tilted = []

  for col in range(num_cols - 1, -1, -1):
    row = 0
    new_row = []
    while col < num_cols and row < num_rows:
      new_row.append(matrix[row][col])
      row += 1
      col += 1
    tilted.append("".join(new_row))
  for row in range(1, num_rows):
    col = 0
    new_row = []
    while col < num_cols and row < num_rows:
      new_row.append(matrix[row][col])
      row += 1
      col += 1
    tilted.append("".join(new_row))
  return tilted

def tilt_right(matrix):
  num_cols = len(matrix[0])
  num_rows = len(matrix)
  tilted = []

  for col in range(num_cols - 1, -1, -1):
    row = num_rows - 1
    new_row = []
    while col < num_cols and row >= 0:
      new_row.append(matrix[row][col])
      row -= 1
      col += 1
    tilted.append("".join(new_row))
  for row in range(num_rows - 2, -1, -1):
    col = 0
    new_row = []
    while col < num_cols and row >= 0:
      new_row.append(matrix[row][col])
      row -= 1
      col += 1
    tilted.append("".join(new_row))
  return tilted

def part1():
  lines = read_input(4, False)
  num_cols = len(lines[0])
  num_rows = len(lines)

  occurrences = 0
  for row in range(num_rows):
    occurrences += len(re.findall(r"XMAS", lines[row]))
    occurrences += len(re.findall(r"XMAS", lines[row][::-1]))

  for col in range(num_cols):
    search_string = "".join([lines[row][col] for row in range(num_rows)])
    occurrences += len(re.findall(r"XMAS", search_string))
    occurrences += len(re.findall(r"XMAS", search_string[::-1]))

  left_tilted = tilt_left(lines)
  for line in left_tilted:
    occurrences += len(re.findall(r"XMAS", line))
    occurrences += len(re.findall(r"XMAS", line[::-1]))

  right_tilted = tilt_right(lines)
  for line in right_tilted:
    # the middle line is shared between the two tilted matrices, so we skip it
    # if len(line) == 10:
    #   continue
    occurrences += len(re.findall(r"XMAS", line))
    occurrences += len(re.findall(r"XMAS", line[::-1]))

  return occurrences

def part2():
  lines = read_input(4, False)

  occurrences = 0
  for row in range(len(lines) - 2):
    for col in range(len(lines[row]) - 2):
      diag1 = lines[row][col] + lines[row + 1][col + 1] + lines[row + 2][col + 2]
      diag2 = lines[row][col + 2] + lines[row + 1][col + 1] + lines[row + 2][col]
      if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
        occurrences += 1
  return occurrences


if __name__ == '__main__':
  # print(part1())
  print(part2())
