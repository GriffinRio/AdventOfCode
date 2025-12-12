def main():
  #input = open("puzzle21&22_input.txt")
  input = open("example2.txt")
  deviceConnections = {}
  for line in input:
    line = line.strip().split(":")
    deviceConnections[line[0]] = line[1].split()
  start = ["svr"]
  pathsToDac = findPathsThrough(deviceConnections, start, "dac")
  pathsToFft = findPathsThrough(deviceConnections, start, "dac")
  pathsOutFromDac = findPathsOut(deviceConnections, "dac")
  pathsOutFromFft = findPathsOut(deviceConnections, "fft")
  
  allPaths = 0
  for i in range(len(pathsThrough)):
    allPaths += len(pathsThrough[i]) * len(pathsOut[i])
  print(len(pathsThrough))

def findPathsOut(links: list, path: list):
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
      foundPaths = findPathsOut(links,newPath)
      for found in foundPaths:
        allPaths.append(found)
  if(edgeFound):
    return allPaths
  
def findPathsThrough(links: list, path: list, goal):
  if(goal in links[path[-1]]):
    path.append(goal)
    return [path]
  allPaths = []
  connections = links[path[-1]]
  edgeFound = False
  for edge in connections:
    if(edge not in path and edge != "out"):
      edgeFound = True
      newPath = path.copy()
      newPath.append(edge)
      foundPaths = findPathsThrough(links, newPath, goal) or []
      for found in foundPaths:
        allPaths.append(found)
  if(edgeFound):
    return allPaths


  
main()