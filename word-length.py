# inp = "Python is very very easy language"
# out = {word.lower(): len(word) for word in inp.split()}
# print(out)

# ord('a')
# chr(97)

inp = "Hai HeLLO"
out = {i:ord(i) for i in inp if ord(i)>64 and ord(i)<91}
print(out)