def main():
  input = open("puzzle3&4_input.txt")
  #input = open("example.txt")
  ranges = input.read()
  input.close()
  ranges = ranges.split(",")
  invalids = []
  for range in ranges:
    foundInvalids = findInvalids(range)
    invalids = [*invalids, *foundInvalids]
  sum = 0
  for invalid in invalids:
    sum += int(invalid)
  print(sum)
  
def findInvalids(range):
  start, end = range.split("-")
  start, end = int(start), int(end)
  current = start
  found = []
  while(current <= end):
    current = str(current)
    length = len(current)
    if(length % 2 == 0):
      first, second = current[:(length//2)], current[(length//2):]
      if(first == second):
        found.append(current)
    current = int(current) + 1
  
  return found

main()