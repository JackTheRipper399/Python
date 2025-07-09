# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuples = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = {"apple", "orange", "banana", "coconut"}
fruits = ("apple", "orange", "banana", "coconut")

# print(fruits[0:3])
# print(dir(fruits))
# print(help*fruits)
# print(len(fruits))
# print("pineapple" in fruits)

# Lists
# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))
"""for fruit in fruits:
    print(fruit)"""

# Sets
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

# Tuples
print(fruits.index("apple"))
print(fruits.count("coconut"))
