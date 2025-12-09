def main():
  input = open("puzzle13&14_input.txt")
  #input = open("example.txt")
  past = list(input.readline().strip())
  splits = 0
  for line in input:
    splitsFound, past = calculateBeams(past, list(line.strip()))
    splits += splitsFound 
  print(splits)

def calculateBeams(past, current):
  splitsFound = 0
  for i in range(len(past)):
    if(past[i] == "|" or past[i] == "S"):
      if(current[i] == "." ):
        current[i] = "|"
      elif(current[i] == "^"):
        splitsFound += 1
        if(i + 1 < len(current) and current[i + 1] != "^"):
          current[i + 1] = "|"
        if(i - 1 > 0 and current[i - 1] != "^"):
          current[i - 1] = "|"
  return splitsFound, current


main()