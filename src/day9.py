import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()

  return lines[0]

def part1():
  input = read_input(9, False)

  file_id = 0
  is_file = True
  blocks = []
  for char in input:
    if is_file:
      for i in range(0, int(char)):
        blocks.append(str(file_id))
      file_id += 1
      is_file = False
    else:
      for i in range(0, int(char)):
        blocks.append('.')
      is_file = True
  
  compacted = []
  front = 0
  back = len(blocks) - 1
  is_front = True
  free_space = 0
  while front <= back:
    if is_front:
      if blocks[front] != '.':
        if free_space == 0:
          compacted.append(blocks[front])
          front += 1
        else:
          is_front = False
      else:
        free_space += 1
        front += 1
    else:
      if free_space > 0:
        if blocks[back] != '.':
          compacted.append(blocks[back])
          free_space -= 1
          back -= 1
        else:
          back -= 1
      else:
        is_front = True

  checksum = 0
  for i in range(0, len(compacted)):
    if compacted[i] == '.':
      break
    checksum += i*int(compacted[i])
  return checksum

def part2():
  input = read_input(9, True)
  
  file_id = 0
  is_file = True
  blocks = []
  dot_index = {}
  for char in input:
    if is_file:
      if char != '0':
        blocks.append(int(char)*str(file_id))
      file_id += 1
      is_file = False
    else:
      if char != '0':
        blocks.append(int(char)*'.')
        if int(char) not in dot_index:
          dot_index[int(char)] = []
        dot_index[int(char)].append(len(blocks)-1)
      is_file = True
  
  # maybe I need to maintain some kind of index of where dots are instead of searching for them every time?
  for back in range(len(blocks)-1, -1, -1):
    if blocks[back].startswith('.'):
      continue
    for front in range(0, back):
      if blocks[front].startswith('.'):
        if len(blocks[back]) < len(blocks[front]):
          blocks.insert(front, blocks[back])
          back += 1
          blocks[front+1] = '.'*(len(blocks[front+1]) - len(blocks[back]))
          blocks[back] = '.'*len(blocks[back])
          break
        elif len(blocks[front]) == len(blocks[back]):
          blocks[front], blocks[back] = blocks[back], blocks[front]
          break

  checksum = 0
  compacted = "".join(blocks)
  for i in range(0, len(compacted)):
    if compacted[i] != '.':
      checksum += i*int(compacted[i])
  return checksum

if __name__ == '__main__':
  # print(part1())
  print(part2())
