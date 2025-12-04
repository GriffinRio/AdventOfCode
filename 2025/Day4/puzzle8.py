def main():
  input = open("puzzle7&8_input.txt")
  #input = open("example.txt")
  firstInput = []
  for line in input:
    firstInput.append(line.strip())
  input.close
  removed = 0
  done = False
  found, adjacent = roundOfRemoval(firstInput)
  while(not done):
    if(found > 0):
      removed += found
      nextInput = []
      nextLine = ""
      for line in adjacent:
        for point in line:
          if(point == -1 or point < 4):
            nextLine = nextLine + "."
          else:
            nextLine = nextLine +"@"
        nextInput.append(nextLine)
        nextLine = ""
      found, adjacent = roundOfRemoval(nextInput)
    else:
      done = True
  print(removed)

def roundOfRemoval(input: list):
  current = input.pop(0)
  forkliftable = 0
  adjacent = [([0] * len(current))]
  for line in input:
    adjacent.append(([0] * len(current)))
    forkliftable += findForkliftable(current, line, adjacent)
    current = line
  for i in range(len(current) - 1):
    if(current[i] == "@"):
      if(current[i + 1] == "@"):
        adjacent[-1][i] += 1
        adjacent[-1][i + 1] += 1
        
      if(adjacent[-1][i] < 4):
        forkliftable += 1
    else:
       adjacent[-1][i] = -1
  if(current[-1] == "@"):     
    if(adjacent[-1][-1] < 4):
      forkliftable += 1
  else:
    adjacent[-1][-1] = -1
  
  return forkliftable, adjacent


def findForkliftable(current: str, next: str, adjacent):
  found = 0
  if(current[0] == "@"):
    if(current[1] == "@"):
        adjacent[-2][0] += 1
        adjacent[-2][1] += 1
    if(next[0] == "@"):
        adjacent[-2][0] += 1
        adjacent[-1][0] += 1
    if(next[1] == "@"):
        adjacent[-2][0] += 1
        adjacent[-1][1] += 1

    if(adjacent[-2][0] < 4):
        found += 1
  else:
    adjacent[-2][0] = -1

  for i in range(1, len(current) - 1):
    if(current[i] == "@"):
      if(current[i + 1] == "@"):
        adjacent[-2][i] += 1
        adjacent[-2][i + 1] += 1
      for j in range (-1, 2):
        if(next[i + j] == "@"):
          adjacent[-2][i] += 1
          adjacent[-1][i + j] += 1

      if(adjacent[-2][i] < 4):
        found += 1
    else:
      adjacent[-2][i] = -1

  if(current[-1] == "@"):
    for j in range (-1, 1):
        if(next[-1 + j] == "@"):
          adjacent[-2][-1] += 1
          adjacent[-1][-1 + j] += 1

    if(adjacent[-2][-1] < 4):
        found += 1
  else:
    adjacent[-2][-1] = -1

  return found


main()