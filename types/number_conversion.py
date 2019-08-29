integer_type = 242424
float_type = 3.17
complex_type = 676j

anIntegerConvertedToFloat = float(integer_type)
print(anIntegerConvertedToFloat)  # 242424.0
print(type(anIntegerConvertedToFloat))  # <class 'float'>

aFloatConvertedToInteger = int(float_type)
print(aFloatConvertedToInteger)  # 3
print(type(aFloatConvertedToInteger))  # <class 'int'>

anIntegerConvertedToComplex = complex(integer_type)
print(anIntegerConvertedToComplex)  # (242424+0j)
print(type(anIntegerConvertedToComplex))  # <class 'complex'>


# Casting

def print_vars(x, y, z, w):
    print(x)
    print(y)
    print(z)
    print(w)
    print('\n')


def cast_to_int():
    x = int(1)  # x will be 1
    y = int(2.8)  # y will be 2
    z = int("3")  # z will be 3
    print_vars(x, y, z, '')


def cast_to_float():
    x = float(1)  # x will be 1.0
    y = float(2.8)  # y will be 2.8
    z = float("3")  # z will be 3.0
    w = float("4.2")  # w will be 4.2
    print_vars(x, y, z, w)


def cast_to_str():
    x = str("s1")  # x will be 's1'
    y = str(2)  # y will be '2'
    z = str(3.0)  # z will be '3.0'
    print_vars(x, y, z, '')


cast_to_int()
cast_to_float()
cast_to_str()
