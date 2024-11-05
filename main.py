text = "hello"
file = open("databaze.txt", "a")
file.write(text)
file.close()

file = open("databaze.txt", "r")
output = file.read()
file.close()

print(output)

with open("databaze2.special", "w") as f:
    f.writelines(["lines\n", "line2"])

with open("databaze2.special", "r") as f:
    text = f.readlines()
    print(text)