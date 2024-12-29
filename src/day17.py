import copy
from functools import cache
from itertools import chain
import re
from queue import PriorityQueue

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.read().strip().split('\n')
  
  registers = {}
  program = []
  for line in lines:
    if line.startswith('Register'):
      reg, val = line.split(': ')
      registers[reg.split()[1]] = int(val)
    elif line.startswith('Program'):
      program = list(map(int, line.split(': ')[1].split(',')))
  
  return registers, program

def adv(registers, operand):
  registers['A'] //= 2 ** operand

def bxl(registers, operand):
  registers['B'] ^= operand

def bst(registers, operand):
  registers['B'] = operand % 8

def bxc(registers, operand):
  registers['B'] ^= registers['C']

def out(registers, operand):
  return operand % 8

def bdv(registers, operand):
  registers['B'] = registers['A'] // (2 ** operand)

def cdv(registers, operand):
  registers['C'] = registers['A'] // (2 ** operand)

def get_operand_value(registers, operand):
  if operand < 4:
    return operand
  elif operand == 4:
    return registers['A']
  elif operand == 5:
    return registers['B']
  elif operand == 6:
    return registers['C']
  else:
    raise ValueError("Invalid combo operand")

def part1():
  input = read_input(17, False)
  registers, program = input

  result = []
  instruction_pointer = 0
  while instruction_pointer < len(program):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]
    if opcode == 0:
      adv(registers, get_operand_value(registers, operand))
    elif opcode == 1:
      bxl(registers, operand)
    elif opcode == 2:
      bst(registers, get_operand_value(registers, operand))
    elif opcode == 3:
      if registers['A'] != 0:
        instruction_pointer = operand
        continue
    elif opcode == 4:
      bxc(registers, operand)
    elif opcode == 5:
      result.append(out(registers, get_operand_value(registers, operand)))
    elif opcode == 6:
      bdv(registers, get_operand_value(registers, operand))
    elif opcode == 7:
      cdv(registers, get_operand_value(registers, operand))
    else:
      raise ValueError("Invalid opcode")
    instruction_pointer += 2
  
  return ",".join(map(str, result))

def run_program(registers, program):
  result = []
  instruction_pointer = 0
  while instruction_pointer < len(program):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]
    if opcode == 0:
      adv(registers, get_operand_value(registers, operand))
    elif opcode == 1:
      bxl(registers, operand)
    elif opcode == 2:
      bst(registers, get_operand_value(registers, operand))
    elif opcode == 3:
      if registers['A'] != 0:
        instruction_pointer = operand
        continue
    elif opcode == 4:
      bxc(registers, operand)
    elif opcode == 5:
      result.append(out(registers, get_operand_value(registers, operand)))
    elif opcode == 6:
      bdv(registers, get_operand_value(registers, operand))
    elif opcode == 7:
      cdv(registers, get_operand_value(registers, operand))
    else:
      raise ValueError("Invalid opcode")
    instruction_pointer += 2

    if result != program[:len(result)]:
      return False
    
  return result == program
  # return result
  

def list_similarity(list1, list2):
  matches = sum(1 for a, b in zip(list1, list2) if a == b)
  return matches / max(len(list1), len(list2))

def part2():
  # similarities = {}
  # for i in range(11):
  #   i = 10_000_000 * i
  #   input = read_input(17, False)
  #   registers, program = input
  #   registers['A'] = i
  #   result = run_program(registers, program)
  #   similarities[i] = list_similarity(result, program)

  
  i = 10_000_000
  solved = False
  while not solved:
    input = read_input(17, False)
    registers, program = input
    registers['A'] = i
    
    solved = run_program(registers, program)
    i += 1

  return i

if __name__ == '__main__':
  # print(part1())
  print(part2())
