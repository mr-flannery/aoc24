import copy
from functools import cache
from itertools import chain
import re
from queue import PriorityQueue

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read()

  towels, patterns = lines.split('\n\n')

  towels = towels.rstrip().split(', ')
  patterns = patterns.rstrip().split('\n')

  return towels, patterns

def part1():
  input = read_input(19, False)
  towels, patterns = input

  @cache
  def match_pattern(pattern):
    if not pattern:
      return True
    for towel in towels:
      if pattern.startswith(towel):
        if match_pattern(pattern[len(towel):]):
          return True
    return False

  valid_patterns = 0
  for pattern in patterns:
      if match_pattern(pattern):
          valid_patterns += 1
  return valid_patterns

def part2():
  input = read_input(19, False)
  towels, patterns = input

  @cache
  def match_pattern(pattern):
    if not pattern:
      return 1
    
    return sum(match_pattern(pattern[len(towel):]) for towel in towels if pattern.startswith(towel))

  return sum(match_pattern(pattern) for pattern in patterns)

if __name__ == '__main__':
  # print(part1())
  print(part2())
