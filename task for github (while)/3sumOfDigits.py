num = eval(input("Enter a number : "))
sumdig = num
leng = len(str(num))
while leng>1:
    num = sumdig
    sumdig = 0
    while num>0:
        rem = num%10
        sumdig+=rem
        num=num//10
    leng = len(str(sumdig))
    # print("length : ", leng)
print("The sum is : ",sumdig)