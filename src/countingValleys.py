def countingValleys(steps, path):
    level = 0
    valleys = 0

    for steps in path:
        if steps =='U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1

    return valleys

steps = 8
path = "UDDDUDUU"
print("numero de valles:", countingValleys(steps, path))