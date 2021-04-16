def parseBeliefs(line):
    try:
        belief = [float(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5])]
        return belief
    except:
        raise ValueError('The values of beliefs should be of type float')

def getInput():
    with open(sys.argv[1], "r") as file:
        lines, input = file.readlines(), []
        for ln in lines:
            if ln != '\n':
                ln, line = ln.split('\n')[0].split(' '), []
                for char in ln:
                    if char:
                        line.append(char)
                input.append(line)
    file.close()
    return input

def parseInput(input):
    if len(input) != 5 or len(input[0]) != 2 or len(input[1]) != 2 or len(input[2]) != 6 or len(input[3]) != 6 or len(input[4]) != 6:
        raise ValueError('Incorrect Format!')
    rollNum1 = input[0][0]
    rollNum2 = input[0][1]
    try:
        x, y = float(input[1][0]), int(input[1][1])
        rollNum1_toint = int(rollNum1)
        rollNum2_toint = int(rollNum2)
    except:
        raise ValueError('Roll number, x, y should be of type float or int')
    beliefs = []
    for i in range(3):
        beliefs.append(parseBeliefs(input[i + 2]))

    return rollNum1, rollNum2, x, y, beliefs

def verifyXY(rollNum1, rollNum2, x, y):
    tol = 0.01
    if abs(1 - (int(rollNum1[-4:])%30 + 1)/100 - x) > tol or abs(int(rollNum1[-2:])%4 + 1 - y) > tol:
        if abs(1 - (int(rollNum2[-4:])%30 + 1)/100 - x) > tol or abs(int(rollNum2[-2:])%4 + 1 - y) > tol:
            raise ValueError("Incorrect values of x, y")
        else:
            return rollNum2
    else:
        return rollNum1

def run():
    input = getInput()
    rollNum1, rollNum2, x, y, beliefs = parseInput(input)
    usedRoll = verifyXY(rollNum1, rollNum2, x, y)

    print("Roll Number 1 : ", rollNum1)
    print("Roll Number 2 : ", rollNum2)
    print('Roll Number Used : ', usedRoll)
    print("x, y : ", x, y)
    print("Beliefs : ", beliefs)
    print("Parsed Succesfully!")
    return x, y, beliefs

def eval(x, y, beliefs):
    # HMMMM :P
    pass

if __name__ == "__main__":
    import sys
    x, y, beliefs = run()
    eval(x, y, beliefs)
