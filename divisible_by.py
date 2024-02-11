#user enters starting value then ending value then 3rd value program checks if 3rd value is divisible by any number from range of 1st and second alue. and also prints the result
num1 = int(input("enter 1st numer: "))
num2 = int(input("enter second number: "))
if num1>num2:
    print("please enter 2nd number as greater than 1st")
    exit()
else:
    num3 = int(input("enter 3rd number: "))
    list = []
    for i in range(num1,num2+1):
        if i % num3 == 0:
            list.append(i)
print(list)
