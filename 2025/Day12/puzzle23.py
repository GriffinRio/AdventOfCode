def main():
  #input = open("puzzle23&24_input.txt")
  input = open("example.txt")
  presentShapes = {}
  currentShape = ["...", "...", "..."]
  shapeLine = 0
  shapeNum = int(input.readline()[0])
  trees = []
  for line in input:
    line = line.strip()
    if("x" not in line):
      if(line == ""):
        spaceTaken = 0
        for line in currentShape:
          spaceTaken += line.count("#")
        presentShapes[shapeNum] = [currentShape.copy(), spaceTaken]
        currentShape = ["...", "...", "..."]
        nextLine = input.readline().strip()
        if("x" in nextLine):
          trees.append(nextLine)
        else:
          shapeNum = int(nextLine[0])
          shapeLine = 0
      else:
        currentShape[shapeLine] = line
        shapeLine += 1
    else:
      trees.append(line)
  possibleTrees = []
  for tree in trees:
    info = tree.split(":")
    xIndex = info[0].find("x")
    width = int(info[0][:xIndex])
    length = int(info[0][xIndex + 1:])
    layout = [["."] * width for i in range(length)]
    presentsAmount = [int(num) for num in info[1].split()]
    inventory = {}
    for i in range(len(presentsAmount)):
      if(presentsAmount[i] > 0):
        inventory[i] = presentsAmount[i]
    if(testDecoration(tree, presentShapes)):
      possibleTrees.append(tree)
  print(possibleTrees)


def testDecoration(layout, presents, inventory):
  #test rotational symmetry
  
  
  return False

      

  
    
    
    




main()