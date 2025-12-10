def main():
  input = open("puzzle13&14_input.txt")
  #input = open("example.txt")
  manifold = []
  for line in input:
    manifold.append(line.strip())
  start = [manifold[0]]
  startIndex = start[0].index("S")
  start.append(insertChar(manifold[1],"|", startIndex))
  timelinesToFollow = [start]
  totalTimelines = 0
  while(len(timelinesToFollow) > 0):
    timeline = timelinesToFollow.pop(0)
    timelinesToAdd = followTimeline(timeline, manifold)
    totalTimelines += 1
    for item in timelinesToAdd:
      timelinesToFollow.append(item)
    print(totalTimelines)
  print(totalTimelines)

def followTimeline(timeline : list, manifold):
  newTimelines = []
  for lineIndex in range(len(timeline) - 1, len(manifold) - 1):
    nextLine = manifold[lineIndex + 1]
    beamIndex = timeline[lineIndex].index("|")
    if(nextLine[beamIndex] == "."):
      timeline.append(insertChar(nextLine, "|", beamIndex))
    else:
      left = beamIndex - 1
      right = beamIndex + 1
      if(right < len(nextLine) and nextLine[right] != "^"):
        new = timeline.copy()
        new.append(insertChar(nextLine, "|", right))
        newTimelines.append(new)
      if(left >= 0 and nextLine[left] != "^"):
        timeline.append(insertChar(nextLine, "|", left))
      
  return newTimelines

def insertChar(string, char, index):
  if(index < 0 or index > len(string) or len(char) > 1):
    return ValueError
  stringList = list(string)
  stringList[index] = char
  return "".join(stringList)

main()