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
  digits = [9] * 12
  batteriesLeft = bank

  for i in range(len(digits)):
    if(len(batteriesLeft) == (len(digits) - i)):
      digits[i] = int(batteriesLeft[0])
      batteriesLeft = batteriesLeft[1:]
    else:
      foundDigit = False
      while(not foundDigit):
        index = batteriesLeft.find(str(digits[i]))
        if(index != -1 and (len(batteriesLeft) - (index + 1)) >= (len(digits) - (i + 1))):
          foundDigit = True
          batteriesLeft = batteriesLeft[index + 1:]
        else:
          digits[i] -= 1

  maxJolt = ""
  for digit in digits:
    maxJolt += str(digit)

  return int(maxJolt)

main()