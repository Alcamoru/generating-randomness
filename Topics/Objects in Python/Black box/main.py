test_list = [0, 5, "ab"]

new_list = blackbox(test_list)

if id(new_list) == id(test_list):
    print("modifies")
else:
    print("new")
