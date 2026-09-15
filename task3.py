# 1. Convert integer to a floating-point number
zahl = 10
converted_f = float(zahl)
print("1. Convert integer to a floating-point number")
print ("Original:" , zahl, type(zahl))
print("Converted:", converted_f, type(converted_f))

#2. Convert a floating-point number to an integer
kommazahl = 10.5
converted_int = int(kommazahl)
print("2. Convert a floating-point number to an integer")
print ("Original:" , kommazahl, type(kommazahl))
print("Converted:", converted_int, type(converted_int))

#3. Convert an integer to a string
zahl = 10
converted_str = str(zahl)
print("3. Convert an integer to a string")
print("Original:" , zahl, type(zahl))
print("Converted:", converted_str, type(converted_str))

#4. Convert a string containing a number to an integer
text = "30"
converted_int = int(text)
print("4. Convert a string containing a number to an integer")
print("Original:" , text, type(text))
print("Converted:", converted_int, type(converted_int))

#5. Convert an integer to a Boolean
zahl = 1
converted_bool = bool(zahl)
print("5. Convert an integer to a boolean")
print("Original:" , zahl, type(zahl))
print("Original:" , zahl, type(zahl))
print("Converted:", converted_bool, type(converted_bool))

zahl = 0
converted_bool = bool(zahl)
print("Original:" , zahl, type(zahl))
print("Converted:", converted_bool, type(converted_bool))