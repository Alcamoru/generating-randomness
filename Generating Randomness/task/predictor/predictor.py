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

triads = {'000': [0, 0], '001': [0, 0], '010': [0, 0], '011': [0, 0],
          '100': [0, 0], '101': [0, 0], '110': [0, 0], '111': [0, 0]}

slice_data = []

for i in range(len(data) - 3):
    if data[i + 3] == '0':
        triads[data[i: i + 3]][0] += 1
    else:
        triads[data[i: i + 3]][1] += 1

for key, value in triads.items():
    print(f'{key}: {value[0]},{value[1]}')
