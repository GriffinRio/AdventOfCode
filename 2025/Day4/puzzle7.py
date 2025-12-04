def main():
  input = open("puzzle7&8_input.txt")
  #input = open("example.txt")
  current = input.readline().strip()
  forkliftable = 0
  adjacent = [([0] * len(current))]
  for line in input:
    adjacent.append(([0] * len(current)))
    forkliftable += findForkliftable(current, line.strip(), adjacent)
    current = line.strip()
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
  print(forkliftable)
  input.close()
  

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