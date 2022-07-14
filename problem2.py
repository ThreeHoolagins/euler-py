fourMillion = 4000000
testnum = 100
def isEven(number):
    if number%2==0:
        return True
    return False

# Fibinachi would be in a method but it's easier for purposes of soliving
# the problem to just run it

sum = 0

f1=1
f2=2

while True:
    # print(f"F1:{f1}, F2:{f2}")
    if f2 >= fourMillion:
        break
    if isEven(f2):
        sum+=f2

    temp = f2
    f2+=f1
    f1 = temp


print(sum)
