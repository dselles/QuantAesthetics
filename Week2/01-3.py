# Filtering lists

l = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "cranberry",
    "cantaloupe",
    "clementine",
]

for fruit in l:
    capitalized_fruit = fruit.capitalize()
    print(f"hello, tasty {capitalized_fruit}!")

target_l = []
for fruit in l:
    if "i" in fruit: # contains the letter i
        target_l.append(fruit)
print(target_l)

target_l = []
for fruit in l:
    if fruit[0] == "c": # starts with c
        target_l.append(fruit)
print(target_l)