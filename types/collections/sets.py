# A set is a collection which is unordered and un-indexed.
# In Python sets are written with curly brackets.


a_set_of_color_pens = {'Red Pen', 'Blue Pen', 'Green Pen'}
print(a_set_of_color_pens)  # >> {'Green Pen', 'Red Pen', 'Blue Pen'}

# Loop
for pen in a_set_of_color_pens:
    print(pen)

# Check if pen is in the set
if 'Red Pen' in a_set_of_color_pens:
    print('Red pen is present in the set')
else:
    print('Red pen is not present in the set')

# Add a new pen to the set
a_set_of_color_pens.add('Black Pen')

print(a_set_of_color_pens)  # >> {'Green Pen', 'Black Pen', 'Blue Pen', 'Red Pen'} (Notice the order)
