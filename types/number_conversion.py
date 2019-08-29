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
