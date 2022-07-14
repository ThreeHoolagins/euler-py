def threeorfive (number):
    if number==0:
        return False
    elif number%3==0:
        return True
    elif number%5==0:
        return True
    else:
        return False

maxnum = 1000

sum = 0
for x in range(maxnum):
    if threeorfive(x):
        sum+= x

print(sum)
