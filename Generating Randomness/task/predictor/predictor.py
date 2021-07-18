data = ""

while len(data) < 100:
    print("Print a random string containing 0 or 1:")
    user_input = input()
    for i in user_input:
        if i in "01":
            data += i
    print(f"Current data length is {len(data)}, {100 - len(data)} symbols left")

print("Final data string:")
print(data)
