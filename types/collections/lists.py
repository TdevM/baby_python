# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and un-indexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

numbers_integers = [1, 2, 3, 4, 5]  # a list
string_fruits = ["apple", "banana", "cherry"]

print(numbers_integers)  # >> [1, 2, 3, 5]
print(string_fruits)  # >> ['apple', 'banana', 'cherry']
print(len(numbers_integers))  # >> 5
print('First fruit in the list is: ' + string_fruits[0])  # >> First fruit in the list is: apple
print(
    'Last number in the list is: ' + str(numbers_integers[-1])
)  # >> Last number in the list is: 5 (Negative indexing)

print(numbers_integers[0:3])  # >> [1, 2, 3] (includes starting index and excludes ending index)

list_of_alpha_bets = ['A', 'B', 'C', 'D']
# list_of_alpha_bets[4] = 'E'  # >> IndexError: list assignment index out of range
list_of_alpha_bets[0] = 1
print(list_of_alpha_bets)  # >> [1, 'B', 'C', 'D']

# Looping the list
print('\nLooping...\n')
for x in string_fruits:
    print(x)

# Append to a list
list_of_alpha_bets.append('E')
print(list_of_alpha_bets)  # >> [1, 'B', 'C', 'D', 'E'] (Adds E to the end of the list)

# Insert into the list
list_of_alpha_bets.insert(1, '2')
print(list_of_alpha_bets)  # >> [1, '2', 'B', 'C', 'D', 'E'] (Inserts 2 between list at index 2)
