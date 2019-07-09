f=open("testText.txt", "a")
print("This is a new sentence", file=f)
print("Tacos is life", file=f)
print("Tacos is love", file=f)
#print(f.readlines())

f.close()