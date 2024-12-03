from functools import reduce

def read_input():
  with open('input/day1.txt') as f:
    lines = f.readlines()

  # list1 = [3,4,2,1,3,3]
  # list2 = [4,3,5,3,9,3]
  list1 = []
  list2 = []

  for line in lines:
    a,b = line.split("   ")
    list1.append(int(a))
    list2.append(int(str.strip(b)))
  return list1, list2

def part1():
  list1, list2 = read_input()
  sorted_list_1 = sorted(list1)
  sorted_list_2 = sorted(list2)

  distances = []
  for a,b in zip(sorted_list_1, sorted_list_2):
    distances.append(abs(a-b))
  result = reduce(lambda x,y: x+y, distances)
  return result

def part2():
  list1, list2 = read_input()
  
  histogram = {}
  for num in list2:
    if num in histogram:
      histogram[num] += 1
    else:
      histogram[num] = 1
  
  result = 0
  for num in list1:
    if num in histogram:
      result += num * histogram[num]
  
  return result

if __name__ == '__main__':
  print(part1())
  print(part2())
