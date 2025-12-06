def main():
  #input = open("puzzle11&12_input.txt")
  input = open("example.txt")
  firstLine = input.readline()
  firstNumbers = firstLine.split()
  expressions = []
  for number in firstNumbers:
    expressions.append([number])
  for line in input:
    lineSplit = line.split()
    for i in range(len(lineSplit)):
      expressions[i].append(lineSplit[i])
  calculations = calculateExpressions(expressions)
  total = 0
  for calculation in calculations:
    total += calculation
  print(total)

def calculateExpressions(expressions: list):
  calculations = []
  for expression in expressions:
    calculation = 0
    operator = expression[-1]
    if(operator == "+"):
      for number in expression[:-1]:
        calculation += int(number)
    else:
      calculation = 1
      for number in expression[:-1]:
        calculation *= int(number)
    calculations.append(calculation)
  return calculations

      

main()