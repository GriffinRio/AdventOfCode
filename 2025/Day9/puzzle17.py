def main():
  input = open("puzzle17&18_input.txt")
  #input = open("example.txt")
  tiles = []
  for line in input:
    tile = line.strip().split(",")
    tile = [int(num) for num in tile]
    tiles.append(tile)
  areas = allAreas(tiles)
  sortedAreas = sorted(areas.items(), key= (lambda item : item[1]), reverse=True)

  print(sortedAreas[0])

def allAreas(tiles):
  areas = {}
  for i in range(len(tiles)):
    for j in range(len(tiles)):
      if(not areas.get(f"{j},{i}")):
        areas[f"{i},{j}"] = calculateRectangle(tiles[i], tiles[j])
  return areas

def calculateRectangle(pointOne, pointTwo):
  length = abs(pointOne[0] - pointTwo[0]) + 1
  width =  abs(pointOne[1] - pointTwo[1]) + 1
  return length * width

main()