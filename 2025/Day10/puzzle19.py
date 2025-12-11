def main():
  input = open("puzzle19&20_input.txt")
  #input = open("example.txt")
  shortestCombos = []
  for line in input:
    machine = line.strip().split()
    config = list(machine[0])[1:-1]
    buttons = [group[1:-1].split(",") for group in machine[1:-1]]
    buttons = [[int(light) for light in button] for button in buttons]
    blank = ["."] * len(config)
    shortest = findShortestCombo(config, buttons, blank, [""], float("inf")) - 1
    print(shortest)
    shortestCombos.append(shortest)
  print(sum(shortestCombos))

def findShortestCombo(config, buttons, indicator, combo: list, shortest):
  if(config == indicator or len(combo) >= shortest):
    return len(combo)
  grades = []
  for button in buttons:
    if(combo[-1] != button):
      executed = executeButton(indicator, button)
      grades.append([gradeAction(config, executed), button, executed])
  grades.sort(reverse=True)
  for action in grades:
    nextCombo = combo.copy()
    nextCombo.append(action[1])
    lengthOfSolution = findShortestCombo(config, buttons, executeButton(indicator, action[1]), nextCombo, shortest)
    if(lengthOfSolution < shortest):
      shortest = lengthOfSolution
  return shortest
  
def executeButton(indicator: list, button):
  exectuted = indicator.copy()
  for light in button:
    if(exectuted[light] == "."):
      exectuted[light] = "#"
    else:
      exectuted[light] = "."
  return exectuted

def gradeAction(goal, current):
  grade = 0
  if(goal == current):
    grade = 100
  else:
    for i in range(len(current)):
      if(current[i] == "#"):
        if(goal[i] == "#"):
          grade += 2
        else:
          grade -= 2
      else:
        if(goal[i] == "#"):
          grade -= 2
        else:
          grade += 1

  return grade


main()