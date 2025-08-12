people = {"A1": 2, "B1": 5, "C1": 3}
for key in people:
    print("Key:", key)

for value in people.values():
    print("Value:", value)

for key, value in people.items():
    print(f"{key} -> {value}")
