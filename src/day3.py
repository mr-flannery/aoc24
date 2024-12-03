import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.readlines()

  return lines

def part1():
  lines = read_input(3, False)
  sum = 0
  for line in lines:
    for match in re.findall(r"mul\(\d+,\d+\)", line):
      a,b = re.findall(r"\d+", match)
      sum += int(a) * int(b)
  return sum

def part2():
  lines = read_input(3, False)

  sum = 0
  do = True
  for line in lines:
    instructions = re.findall(r"(?:mul\(\d+,\d+\))|(?:do\(\))|(?:don't\(\))", line)
    for match in instructions:
      if match == "do()":
        do = True
      elif match == "don't()":
        do = False
      else:
        if do:
          a,b = re.findall(r"\d+", match)
          sum += int(a) * int(b)
  return sum


if __name__ == '__main__':
  # print(part1())
  print(part2())
