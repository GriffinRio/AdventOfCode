def main():
  input = open("puzzle9&10_input.txt")
  #input = open("example.txt")
  id_ranges = []
  available_ids = []
  blankFound = False
  for line in input:
    if(line == "\n"):
      blankFound = True
    elif(blankFound):
      available_ids.append(int(line.strip()))
    else:
      id_range = []
      split = line.split("-")
      id_range.append(int(split[0]))
      id_range.append(int(split[1].strip()))
      id_ranges.append(id_range)
  
  combinedRanges = combineRanges(id_ranges)
  fresh = checkFreshness(combinedRanges, available_ids)
  print(fresh)
  

def combineRanges(id_ranges: list):
  combinedRanges = [id_ranges[0]]
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
              toBeRemoved = []
              for j in range(i + 1, len(combinedRanges)):
                if(id_range[1] >= combinedRanges[j][0]):
                  toBeRemoved.append(j)
                  if(id_range[1] < combinedRanges[j][1]):
                    combinedRanges[i][1] = combinedRanges[j][1]
                    break
                else:
                  break
              for index in toBeRemoved:
                combinedRanges.pop(index)
          else:
            combinedRanges.insert(i, id_range)
          spotFound = True
        elif(id_range[0] <= combinedRanges[i][1]):
          if(id_range[1] > combinedRanges[i][1]):
            combinedRanges[i][1] = id_range[1]
            toBeRemoved = []
            for j in range(i + 1, len(combinedRanges)):
              if(id_range[1] >= combinedRanges[j][0]):
                toBeRemoved.append(j)
                if(id_range[1] < combinedRanges[j][1]):
                  combinedRanges[i][1] = combinedRanges[j][1]
                  break
              else:
                break
            for index in toBeRemoved:
              combinedRanges.pop(index)
          spotFound = True
        else:
          i += 1
      else:
        combinedRanges.append(id_range)
        spotFound = True
  return combinedRanges

def checkFreshness(combinedRanges: list, available_ids: list):
  freshCount = 0
  for id in available_ids:
    for id_range in combinedRanges:
      if(id < id_range[0]):
        break
      elif(id > id_range[1]):
        continue
      freshCount += 1
      break
  return freshCount

main()