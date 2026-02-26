num = eval(input("Enter a number : "))
even = 0
odd = 0
while num>0:
    rem = num%10
    if rem%2 == 0:
        even += 1
    else:
        odd += 1
    num = num//10
print("The number of even digits is : ",even)
print("and the number of odd digits is : ",odd)