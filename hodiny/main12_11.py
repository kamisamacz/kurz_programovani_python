FILE_PATH = ("test.ca0")
zdroj = input("zadej slovo")
if len(zdroj) > 4:
    with open(FILE_PATH, "a") as f:
        f.write(f"{zdroj}\n")

with open(FILE_PATH, "r") as f:
    data = f.read()

print(data)