def main():
  input = open("puzzle3&4_input.txt")
  #input = open("example.txt")
  ranges = input.read()
  input.close()
  ranges = ranges.split(",")
  invalids = []
  for id_range in ranges:
    foundInvalids = findInvalids(id_range)
    invalids = [*invalids, *foundInvalids]
  sum = 0
  for invalid in invalids:
    sum += int(invalid)
  print(sum)
  
def findInvalids(id_range):
  start, end = id_range.split("-")
  start, end = int(start), int(end)
  current = start
  found = []
  while(current <= end):
    current = str(current)
    for i in range(len(current) // 2):
      repeat = current[:(i + 1)]
      repeated = ""
      while(len(repeated) < len(current)):
        repeated += repeat
      if(repeated == current):
        found.append(current)
        break
    current = int(current) + 1
  
  return found

main()