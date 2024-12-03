def read_input():
  with open('input/day2.txt') as f:
    lines = f.readlines()

  reports = []
  for line in lines:
    reports.append(list(map(lambda x: int(x), line.split(" "))))
  return reports

def part1():
  reports = read_input()
  
  def is_safe(report):
    if report[0] > report[1]:
      compare = lambda x,y: x > y
    else:
      compare = lambda x,y: x < y

    for i in range(0, len(report)-1):
      if not compare(report[i], report[i+1]) or abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
        return False
    return True
  
  result = 0
  for report in reports:
    if is_safe(report):
      result += 1
  return result

def part2():
  reports = read_input()
  
  # def is_safe(report):
  #   higher, lower = 0, 0
  #   for i in range(0, len(report)-1):
  #     if report[i] > report[i+1]:
  #       higher += 1
  #     else:
  #       lower += 1
  #   if higher > lower:
  #     compare = lambda x,y: x > y
  #   else:
  #     compare = lambda x,y: x < y

  #   removed_level = False
  #   for i in range(0, len(report)-1):
  #     if not compare(report[i], report[i+1]) or abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
  #       if removed_level:
  #         return False
  #       else:
  #         if i+2 < len(report) and (not compare(report[i], report[i+2]) or abs(report[i] - report[i+2]) < 1 or abs(report[i] - report[i+2]) > 3):
  #           return False
  #         else:
  #           removed_level = True
  #           i += 1
  # return True

  def is_safe(report, rec=False):
    if report[0] > report[1]:
      compare = lambda x,y: x > y
    else:
      compare = lambda x,y: x < y

    for i in range(0, len(report)-1):
      if not compare(report[i], report[i+1]) or abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
        if not rec:
          for j in range(0, len(report)):
            if is_safe(report[:j] + report[j+1:], True):
              return True
          return False
        else:
          return False
    return True
  
  
  result = 0
  unsafe_reports = []
  for report in reports:
    if is_safe(report):
      result += 1
    else:
      unsafe_reports.append(report)
  # print(unsafe_reports)
  return result

if __name__ == '__main__':
  # print(part1())
  print(part2())
