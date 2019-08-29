# Strings are Arrays
# strings in Python are arrays of bytes representing unicode characters

one_character_string = 'a'
print(one_character_string[0])  # >> a

two_character_string = 'ab'
print(len(two_character_string))  # >> 2  (No boxing shit)


# Formatting a string (or string builder)
def build_an_order():
    quantity = 3
    item_no = 567
    price = 49.95
    my_order = "I want {} pieces of item {} for {} dollars."
    my_no_mistakes_order = "I have {2} dollars. give me {0} of {1}"
    print(my_no_mistakes_order.format(quantity, item_no, price))
    print(my_order.format(quantity, item_no, price))


build_an_order()
