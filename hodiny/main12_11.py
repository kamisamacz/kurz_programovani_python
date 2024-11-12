FILE_PATH = ("test.ca0")

f =  open(FILE_PATH, "w")
f.write("ahoj vole")
f.close()

f =  open(FILE_PATH, "r")
data = f.read()
f.close()

print(data)