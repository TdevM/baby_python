# A tuple is a collection which is ordered and unchangeable.
# In Python tuples are written with round brackets.


a_tuple_of_fruit = ("apple", "banana", "cherry")
print(a_tuple_of_fruit)
print('First fruit is: ' + a_tuple_of_fruit[0])
print('Last fruit is: ' + a_tuple_of_fruit[-1])

a_tuple_of_fruit[0] = 'a'  # >> TypeError: 'tuple' object does not support item assignment
