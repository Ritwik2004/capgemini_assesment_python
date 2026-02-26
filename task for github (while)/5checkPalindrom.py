num = eval(input("Enter a number : "))
cnum = num
revnum = 0
while num>0:
    rem = num%10
    revnum=revnum*10+rem
    num = num//10
if revnum==cnum:
    print("The number is palindrome...")
else:
    print("The number is not palindrome...")