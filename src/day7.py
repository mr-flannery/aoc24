import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    lines = f.readlines()

  input = []
  for line in lines:
    line = line.strip()
    r, nums = line.split(': ')
    r = int(r)
    nums = list(map(int, nums.split(' ')))
    input.append((r, nums))
  return input

def part1():
  input = read_input(7, False)

  possible_results = []
  for r, nums in input:
    for i in range(0, pow(2,len(nums)-1)):
      operator_string = f'{i:016b}'[16-(len(nums)-1):]

      result = nums[0]
      for j in range(0, len(operator_string)):
        if operator_string[j] == '0':
          result = result + nums[j+1]
        else:
          result = result * nums[j+1]
      if result == r:
        possible_results.append(r)
        break
    
  return sum(possible_results)

def ternary(n):
    e = n//3
    q = n%3
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return ternary(e) + str(q)

def part2():
  input = read_input(7, False)

  possible_results = []
  for r, nums in input:
    for i in range(0, pow(3,len(nums)-1)):
      operator_string = ternary(i)
      operator_string = '0'*(len(nums)-1-len(operator_string)) + operator_string

      result = nums[0]
      for j in range(0, len(operator_string)):
        if operator_string[j] == '0':
          result = result + nums[j+1]
        elif operator_string[j] == '1':
          result = result * nums[j+1]
        else:
          result = int(str(result) + str(nums[j+1]))
      if result == r:
        possible_results.append(r)
        break
    
  return sum(possible_results)


if __name__ == '__main__':
  # print(part1())
  print(part2())
