import re

def read_input(day, sample=False):
  sample_or_real = '.sample' if sample else ''
  with open(f'input/day{day}{sample_or_real}.txt') as f:
    content = f.read()

  rules, updates = content.split('\n\n')

  rules = rules.split('\n')
  rulez = {}
  for rule in rules:
    lhs, rhs = rule.split('|')
    if lhs not in rulez:
      rulez[lhs] = []
    rulez[lhs].append(rhs)
  
  updates = list(filter(lambda l: l != '', updates.split('\n')))
  updatez = []
  for update in updates:
    updatez.append(update.split(','))

  return rulez, updatez

def part1():
  rules, updates = read_input(5, False)
  
  valid_updates = []
  for update in updates:
    violation = False
    for i in range(1, len(update)):
      for j in range(0, i):
        if update[i] in rules and update[j] in rules[update[i]]:
          violation = True
    if not violation:
      valid_updates.append(update)

  sum = 0
  for update in valid_updates:
    sum += int(update[len(update)//2])
  return sum
  
def part2():
  rules, updates = read_input(5, False)
  
  invalid_updates = []
  for update in updates:
    violation = False
    for i in range(1, len(update)):
      for j in range(0, i):
        if update[i] in rules and update[j] in rules[update[i]]:
          violation = True
    if violation:
      invalid_updates.append(update)

  # idea: take all the numbers left of me, and if they're a violation, throw them to the right
  for update in invalid_updates:
    for i in range(1, len(update)):
      for j in range(0, i):
        if update[i] in rules and update[j] in rules[update[i]]:
          update[i], update[j] = update[j], update[i]

  sum = 0
  for update in invalid_updates:
    sum += int(update[len(update)//2])
  return sum


if __name__ == '__main__':
  # print(part1())
  print(part2())
