
fruits = {
    "Apple", "Mango", "Banana", "Orange", "Grapes",
    "Watermelon", "Guava", "Pineapple", "Papaya", "Strawberry"
}


summer_fruits = {
    "Mango", "Banana", "Watermelon", "Papaya", "Pineapple"
}


winter_fruits = {
    "Apple", "Orange", "Grapes", "Guava", "Strawberry"
}


all_fruits = fruits | summer_fruits | winter_fruits
print("All fruits:", all_fruits)



both = summer_fruits & winter_fruits
print("2. Present in both:", both)


only_summer = summer_fruits - fruits
print("3. Only Summer, not in fruits:", only_summer)


both_in_fruits = summer_fruits & winter_fruits & fruits
print("4. Summer and Winter and fruits:", both_in_fruits)


if "Orange" in fruits:
    print("5. Orange is present in fruits")
else:
    print("5. Orange is not present in fruits")


print("6. Pineapple is present in:")

if "Pineapple" in fruits:
    print("Fruits set")

if "Pineapple" in summer_fruits:
    print("Summer fruits set")

if "Pineapple" in winter_fruits:
    print("Winter fruits set")