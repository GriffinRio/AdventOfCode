def main():
  input = open("puzzle21&22_input.txt")
  #input = open("example1.txt")
  deviceConnections = {}
  for line in input:
    line = line.strip().split(":")
    deviceConnections[line[0]] = line[1].split()
  start = ["you"]
  pathsOut = findPaths(deviceConnections, start)
  print(len(pathsOut))

def findPaths(links: list, path: list):
  if("out" in links[path[-1]]):
    path.append("out")
    return [path]
  allPaths = []
  connections = links[path[-1]]
  edgeFound = False
  for edge in connections:
    if(edge not in path):
      edgeFound = True
      newPath = path.copy()
      newPath.append(edge)
      foundPaths = findPaths(links,newPath)
      for found in foundPaths:
        allPaths.append(found)
  if(edgeFound):
    return allPaths

  
main()