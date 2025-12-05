def main():
  input = open("puzzle9&10_input.txt")
  #input = open("example.txt")
  id_ranges = []
  for line in input:
    if(line == "\n"):
      break
    else:
      id_range = []
      split = line.split("-")
      id_range.append(int(split[0]))
      id_range.append(int(split[1].strip()))
      id_ranges.append(id_range)
  
  combinedRanges = combineRanges(id_ranges)
  fresh_ids = countFreshIds(combinedRanges)
  print(fresh_ids)
  

def combineRanges(id_ranges: list):
  combinedRanges = [id_ranges[0]]
  combinesFound = len(id_ranges) - 1
  for id_range in id_ranges[1:]:
    spotFound = False
    i = 0
    while(not spotFound):
      if(i < len(combinedRanges)):
        if(id_range[0] < combinedRanges[i][0]):
          if(id_range[1] >= combinedRanges[i][0]):
            combinedRanges[i][0] = id_range[0]
            if(id_range[1] > combinedRanges[i][1]):
              combinedRanges[i][1] = id_range[1]
          else:
            combinedRanges.insert(i, id_range)
          spotFound = True
        elif(id_range[0] <= combinedRanges[i][1]):
          if(id_range[1] > combinedRanges[i][1]):
            combinedRanges[i][1] = id_range[1]
          spotFound = True
        else:
          i += 1
      else:
        combinedRanges.append(id_range)
        combinesFound -= 1
        spotFound = True
  if(combinesFound == 0):
    return combinedRanges
  else:
    return combineRanges(combinedRanges)

def countFreshIds(combinedRanges: list):
  freshCount = 0
  for id_range in combinedRanges:
    freshCount += (id_range[1] - id_range[0]) + 1
    
  return freshCount

main()