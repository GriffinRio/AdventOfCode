def main():
  input = open("puzzle5&6_input.txt")
  #input = open("example.txt")
  bankJolts = []
  for bank in input:
    joltage = findMaxJoltage(bank.strip())
    bankJolts.append(joltage)
  input.close()
  sum = 0
  for joltage in bankJolts:
    sum += joltage
  print(sum)


def findMaxJoltage(bank: str):
  firstDigit = 9
  secondDigit = 9
  done = False

  while(not done):
    firstIndex = bank.find(str(firstDigit))
    if(firstIndex != -1 and firstIndex + 1 != len(bank)):
      batteriesLeft = bank[firstIndex + 1:]
      while(not done):
        secondIndex = batteriesLeft.find(str(secondDigit))
        if(secondIndex != -1):
          done = True
        else:
          secondDigit -= 1
    else:
      firstDigit -= 1

  maxJolt = str(firstDigit) + str(secondDigit)

  return int(maxJolt)

main()