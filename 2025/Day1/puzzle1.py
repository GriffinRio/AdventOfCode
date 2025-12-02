def main():
  input = open("puzzle1&2_input.txt")
  dial = 50
  zeros = 0
  for line in input:
    dial = rotate(dial, line.replace("\n", ""))
    if(dial == 0):
      zeros += 1
  input.close()
  print(zeros)

def rotate(dial, action):
  direction = action[0]
  turnAmount = int(action[1:])
  if(direction == "L"):
    dial -= turnAmount
  else:
    dial += turnAmount
  dial = dial % 100
  return dial
  

main()
