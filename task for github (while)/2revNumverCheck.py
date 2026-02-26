num = eval(input("Enter the number : "))
cnum = num
revNum = 0
while num>0:
    rem = num%10
    revNum = revNum *10 +rem
    num = num//10
print("The reverse number is : ",revNum)
if cnum<revNum:
    print("the reverse number is greater than the original number...")