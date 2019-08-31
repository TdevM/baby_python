myVariable = 7  # I have just declared a variable of type int here
print(myVariable)  # I can use uppercase in variable names but functions won't allow me to do that.

myVariable = 8
print(myVariable)  # This will now print 8

singleQuotedStringVariable = 'This is a single quoted string variable'  # a string variable
doubleQuotedStringVariable = "This is a double quoted string variable"

print(singleQuotedStringVariable + doubleQuotedStringVariable)  # Concatenation just like JS

okayIAmInteger = 8
print(okayIAmInteger)  # >> 8 (I am a happy integer)
print(type(okayIAmInteger))  # <class 'int'>
okayIAmInteger = 'You will be a string now'
print(type(okayIAmInteger))  # <class 'str'>
print(okayIAmInteger)  # >> You will be a string now  (Woot I'm a string?)

iamasmallcasevariable = 'sometext'
IAMASMALLCASEVARIABLE = 'sometext'

print(id(iamasmallcasevariable))  # >> 4378925616 (Memory address)
print(id(IAMASMALLCASEVARIABLE))  # >> 4378927856 (Memory address)
print(id(iamasmallcasevariable) is id(IAMASMALLCASEVARIABLE))  # >> False
