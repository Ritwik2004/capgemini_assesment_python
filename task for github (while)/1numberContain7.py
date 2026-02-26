# i = 1
# while i<=100:
#     s = str(i)
#     if '7' in s:
#         print(i)
#     i += 1


i = 1
while i <= 100:
    n = i
    found_seven = False
    while n > 0:
        if n % 10 == 7:
            found_seven = True
            break
        n //= 10
    if found_seven:
        print(i)
    i += 1