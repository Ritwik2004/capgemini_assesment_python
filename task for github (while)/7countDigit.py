num = eval(input("Enter the number : "))
digit = eval(input("Enter the digit : "))
count = 0
while num>0:
    rem = num%10
    if rem == digit:
        count+=1
    num = num//10
print("the digit comes ",count," times")