def main():
  input = open("puzzle1&2_input.txt")
  #input  = open("example.txt")
  #input = open("test.txt")
  dial = 50
  zeros = 0
  for line in input:
    dial, zerosFound = slowRotate(dial, line)
    zeros += zerosFound
  input.close()
  print(zeros)

def rotate(dial, action):
  start = dial
  direction = action[0]
  turnAmount = int(action[1:])
  if(direction == "L"):
    dial -= turnAmount
  else:
    dial += turnAmount

  zerosFound = 0
  if(dial == 0):
    zerosFound = 1
  elif(start == 0):
    zerosFound = abs(int(dial / 100))
  else:
    zerosFound = abs(dial // 100)
  
  dial = dial % 100
  
  return dial, zerosFound

def slowRotate(dial, action):
  start = dial
  direction = action[0]
  turnAmount = int(action[1:])
  zerosFound = 0
  operator = 1
  if(direction == "L"):
    operator = -1
  done = False
  while(not done):
    if(turnAmount > 100):
      zerosFound += 1
      turnAmount -= 100
    else:
      dial += operator * turnAmount
      if(start != 0 and (dial <= 0 or dial > 99)):
        zerosFound += 1
      dial = dial % 100
      done = True
  return dial, zerosFound
  


main()