def main():
  input = open("puzzle15&16_input.txt")
  levels = 1000
  #input = open("example.txt")
  #levels = 10
  junctions = []
  for line in input:
    coordinates = line.strip().split(",")
    for index in range(len(coordinates)):
      coordinates[index] = int(coordinates[index])
    junctions.append(coordinates)
  distances = findDistances(junctions)
  sort = sorted(distances.items(), key=(lambda item: item[1]))
  circuits = createCircuits(sort,levels)
  product = 1
  circuitLengths = []
  for group in circuits:
    if(group != "Combined"):
      circuitLengths.append(len(group))
  circuitLengths.sort(reverse=True)
  for i in range(3):
    product *= circuitLengths[i]
  print(product)

def findDistances(junctions):
  distances = {}
  for i in range(len(junctions)):
    for j in range(len(junctions)):
      distance = calculateDistance(junctions[i], junctions[j])
      if(distance != 0 and not distances.get(f"{j},{i}")):
        distances[f"{i},{j}"] = distance
  return distances


def calculateDistance(coordOne, coordTwo):
  squares = []
  for index in range(len(coordOne)):
    squares.append((coordOne[index] - coordTwo[index]) ** 2)
  sum = 0
  for square in squares:
    sum += square
  return sum ** (1/2)

def createCircuits(sortedDistances, levels):
  circuits = []
  connected = {}
  for i in range(levels):
    nextShortest = sortedDistances.pop(0)
    boxes = nextShortest[0].split(",")
    boxes = [int(box) for box in boxes]
    if(len(circuits) == 0):
      circuits.append([boxes[0], boxes[1]])
      connected[boxes[0]] = len(circuits) - 1
      connected[boxes[1]] = len(circuits) - 1
    else:
      boxOneGroup = connected.get(boxes[0])
      boxTwoGroup = connected.get(boxes[1])
      if(boxOneGroup == None and boxTwoGroup == None):
        circuits.append([boxes[0], boxes[1]])
        connected[boxes[0]] = len(circuits) - 1
        connected[boxes[1]] = len(circuits) - 1
      elif(boxOneGroup == boxTwoGroup):
        continue
      elif(boxOneGroup == None):
        circuits[boxTwoGroup].append(boxes[0])
        connected[boxes[0]] = boxTwoGroup
      elif(boxTwoGroup == None):
        circuits[boxOneGroup].append(boxes[1])
        connected[boxes[1]] = boxOneGroup
      else:
        for box in circuits[boxTwoGroup]:
          circuits[boxOneGroup].append(box)
          connected[box] = boxOneGroup
        circuits[boxTwoGroup] = "Combined"
  return circuits

main()