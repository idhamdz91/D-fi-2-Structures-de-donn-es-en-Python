'''Exercice 01 : 

# Step 1: Create a list of favorite fruits
fruits = ["pomme", "banane", "datte", "orange"]

# Step 2: Add a new fruit to the list
fruits.append("raisin")

# Step 3: Remove a fruit from the list
fruits.remove("banane")

# Step 4: Sort the list in alphabetical order
fruits.sort()

# Step 5: Print the list
print(fruits)'''

'''Exercice 2
# Step 1: Create a dictionary representing a person
person = {
    "name": "Mahdi",
    "age": 33,
    "city": "Alger"
}

# Step 2: Add a new key-value pair to the dictionary
person["email"] = "naoui.mahdi@yahoo.fr"

# Step 3: Update one of the values in the dictionary
person["age"] = 33

# Step 4: Print the updated dictionary
print(person)'''

'''Exercice 3
# Step 1: Create two sets of integers
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Step 2: Find the intersection of the sets
intersection = set1 & set2

# Step 3: Find the union of the sets
union = set1 | set2

# Step 4: Print the results
print("Intersection:", intersection)
print("Union:", union)'''

# Step 1: Create a list of numbers
numbers = [10, 25, 38, 42, 59, 73, 88, 91, 100]

# Step 2: Define the number you're searching for
target = 42

# Step 3: Implement the linear search algorithm
def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index  # Return the index if found
    return -1  # Return -1 if not found

# Step 4: Perform the search and print the result
index = linear_search(numbers, target)

if index != -1:
    print(f"Number {target} found at index {index}.")
else:
    print(f"Number {target} not found in the list.")


