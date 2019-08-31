def my_function():
    print('This is a function')
    return 'Yo'


print(my_function)  # This will just print the function address
print(my_function())  # This will print statement inside of the function as well as the result of return


def pass_me_some_snacks(chips, candies, cola):
    thank_you = 'I\'m having {} and {} with {} as my snack today. Thank you for the treat!'
    return thank_you.format(chips, candies, cola)


print(pass_me_some_snacks('Too yumm', 'Mazelo', 'Sprite'))
# >> I'm having Too yumm and Mazelo with Sprite as my snack today. Thank you for the treat!
