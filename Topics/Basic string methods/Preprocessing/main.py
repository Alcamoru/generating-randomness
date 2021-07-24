a = input().lower()
b = ""
for letter in a:
    if letter not in "abcdefghijklmnopqrstuvwxyz ":
        pass
    else:
        b += letter
print(b)
