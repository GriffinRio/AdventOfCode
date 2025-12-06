def main():
  input = open("puzzle11&12_input.txt")
  #input = open("example.txt")
  lines = []
  for line in input:
    lines.append(line.strip("\n"))
  expressions = buildExpressions(lines)
  calculations = calculateExpressions(expressions)
  total = 0
  for calculation in calculations:
    total += calculation
  print(total)

def buildExpressions(lines: list):
  expressions = [[]]
  currentExpression = 0
  for i in range(len(lines[0])):
    column = ""
    for j in range(len(lines)):
      column += lines[j][i]
    column = column.replace(" ", "")
    if(column == ""):
      expressions.append([])
      currentExpression += 1
      continue
    if(column[-1] == "+" or column[-1] == "*"):
      expressions[currentExpression].append(column[-1])
      column = column[:-1]
    expressions[currentExpression].insert(0,int(column))

  return expressions

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