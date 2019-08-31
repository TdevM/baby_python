my_variable = 7
your_variable = 7
enemy_variable = 89991101

# Python Identity Operators

print(my_variable is your_variable)  # >> True
print(my_variable is enemy_variable)  # >> False
print(enemy_variable is not my_variable)  # >> True

meeting_state = True

if not meeting_state:
    print('Meeting is ON')
else:
    print('Meeting is OFF')

x = 71
y = 77

print(x or y)  # >> 71 (Returns the first truthy value.)
print(x and y)  # >> 77 (Returns the first falsy value, else last operand.)
