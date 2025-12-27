'''
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
'''

sample_data = [
  '7 6 4 2 1',
  '1 2 7 8 9',
  '9 7 6 2 1',
  '1 3 2 4 5',
  '8 6 4 4 1',
  '1 3 6 7 9'
]

reports: 'list[list[int]]' = []

def preprocess_data(data: 'list[str]'):
  for line in data:
    reports.append(list(map(int, line.split(' '))))

def part1(data: 'list[str]'):
  preprocess_data(data)

  cnt = 0
  for report in reports:
    if len(report) <= 1:
      cnt += 1
      continue

    diff = report[1] - report[0]
    if diff == 0 or abs(diff) > 3:
      continue

    is_safe = True
    for i in range(2, len(report)):
      next_diff = report[i] - report[i - 1]
      if next_diff == 0 or abs(next_diff) > 3 or diff * next_diff < 0:
        is_safe = False
        break
      
    if is_safe:
      cnt += 1

  print(cnt)

import os

data = []
with open(os.path.join(os.path.dirname(__file__), './input2.txt'), 'r') as file:
  for line in file.readlines():
    data.append(line.strip())

# part1(data)


'''
--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
'''

def is_safe(report: list[int]) -> bool:
  '''
  Check if a report is safe following above constraints, with at most one level removal

  Parameters:
    report (list[int]): a list of levels in a report

  Returns:
    (boolean): Check if the report is safe
  '''

  n = len(report)

  if n <= 1:
    return True

  pre_check = [False] * n
  suf_check = [False] * n

  pre_check[0] = suf_check[-1] = True

  prev_diff = None
  for i in range(1, n):
    diff = report[i] - report[i - 1]
    if diff == 0 or \
      abs(diff) > 3 or \
      (prev_diff is not None and prev_diff * diff) < 0:
      pre_check[i] = False
    else:
      pre_check[i] = pre_check[i - 1]
    
    prev_diff = diff

  if pre_check[-1] is True:
    return True

  prev_diff = None
  for j in range(n - 2, -1, -1):
    diff = report[j] - report[j + 1]

    if diff == 0 or \
      abs(diff) > 3 or \
      (prev_diff is not None and prev_diff * diff) < 0:
      suf_check[j] = False
    else:
      suf_check[j] = suf_check[j + 1]

    prev_diff = diff

  if pre_check[-2] is True or suf_check[1] is True:
    # remove the first or the last level
    return True
  
  for i in range(1, n - 1):
    if pre_check[i - 1] is True and \
      suf_check[i + 1] is True and \
      0 < abs(report[i + 1] - report[i - 1]) <= 3 and \
      (
        (report[i - 2] if i >= 2 else float('-inf')) < report[i - 1] < report[i + 1] < (report[i + 2] if i + 2 < n else float('inf')) or \
        (report[i - 2] if i >= 2 else float('inf')) > report[i - 1] > report[i + 1] > (report[i + 2] if i + 2 < n else float('-inf'))
      ):
      # remove current level
      return True
    
  return False

def part2(data: list[str]):
  preprocess_data(data)

  tot = 0
  for report in reports:
    if is_safe(report):
      tot += 1

  print(tot)

if __name__ == '__main__':
  # part1(data)
  part2(data)
