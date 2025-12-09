def main():
  #input = open("puzzle13&14_input.txt")
  input = open("example.txt")
  start = input.readline().strip()
  firstBlank = list(input.readline().strip())
  firstBlank[start.index("S")] = "|"
  pasts = ["".join(firstBlank)]
  index = 0
  for line in input:
    print(index)
    pasts = calculateBeams(pasts, list(line.strip()))
    index += 1
  print(len(pasts))

def calculateBeams(pasts: str, current: list):
  newTimelines = []
  for past in pasts:
    future = current.copy()
    beamIndex = past.index("|")
    if(current[beamIndex] == "."):
      future[beamIndex] = "|"
    else:
      twoSplits = False
      if(beamIndex + 1 < len(current) and current[beamIndex + 1] != "^"):
        future[beamIndex + 1] = "|"
        twoSplits = True
      if(beamIndex - 1 > 0 and current[beamIndex - 1] != "^"):
        if(twoSplits):
          otherFuture = current.copy()
          otherFuture[beamIndex - 1] = "|"
          newTimelines.append("".join(otherFuture))
        else:
          future[beamIndex - 1] = "|"
    newTimelines.append("".join(future))
  return newTimelines

def followTimeline(timeline):
  print("hi")


main()