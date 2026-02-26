username = "ritwik@"
password = "Kundu@123"
inuser = input("Enter your username : ")
inpass = input("Enter your password : ")
attemp = 1
flag = True
while attemp<=3:
    flag = True
    if(inuser != username):
        flag = False
    if inpass != password:
        flag = False
    if flag == False:
        attemp+=1
        print(attemp)
        inuser = input("Please enter correct username : ")
        inpass = input("Please enter correct password : ")
    else:
        flag = True
        break
if(flag == True):
    print("You are logging in...")
else:
    print("Sorry!!! try again later...")