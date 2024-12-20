import copy
import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().splitlines()

  return lines[0].split(' ')

def part1():
  input = read_input(11, False)

  for i in range(25):
    idx = 0
    while idx < len(input):
      if input[idx] == '0':
        input[idx] = '1'
      elif len(input[idx]) % 2 == 0:
        tmp = input[idx]
        input[idx] = tmp[:len(tmp)//2]
        input.insert(idx+1, str(int(tmp[len(tmp)//2:])))
        idx += 1
      else:
        input[idx] = str(2024 * int(input[idx]))
      idx += 1

  return len(input)

class Node:

  def __init__(self, value):
    self.value = value
    self.children = []

  def expand(self, index):
    # if depth == 0:
    #   return
    
    if not self.children:
      for child_val in apply_rules(self.value):
        if child_val not in index:
          node = Node(child_val)
          index[child_val] = node
          # node.expand(index, depth - 1)
          self.children.append(node)
        else:
          node = index[child_val]
          self.children.append(node)
        # node.expand(index, depth - 1)        
    
    for child in self.children:
      if not child.children:
        child.expand(index)

  def children_at_depth(self, depth, cad_index, index):
    if not self.children:
      self.expand(index)
    
    if depth == 1:
      return len(self.children)
    else:
      sum = 0
      for child in self.children:
        if (child.value, depth - 1) not in cad_index:
          cad_index[(child.value, depth - 1)] = child.children_at_depth(depth - 1, cad_index, index)
        sum += cad_index[(child.value, depth - 1)]
      return sum
  
  def print_children(self, depth):
    if depth == 1:
      for child in self.children:
        print(child.value + " ", end="")
      print()
      return
    
    for child in self.children:
      child.print_children(depth - 1)

def apply_rules(val):
  if val == '0':
    return ['1']
  elif len(val) % 2 == 0:
    return [val[:len(val)//2], str(int(val[len(val)//2:]))]
  else:
    return [str(2024 * int(val))]

def part2():
  input = read_input(11, False)
  
  index = {}
  cad_index = {}

  blinks = 75

  for i in range(len(input)):
    val = input[i]
    if val not in index:
      node = Node(val)
      index[val] = node
      # node.expand(index, blinks)

  sum = 0
  for i in range(len(input)):
    sum += index[input[i]].children_at_depth(blinks, cad_index, index)

  return sum

if __name__ == '__main__':
  # print(part1()) # 172484
  print(part2())
