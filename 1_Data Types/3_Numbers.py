#-----------------------------------Integers-----------------------------------#
print(5*5)
print(5/5)

#-----------------------------------Binary Integers-----------------------------------#
print("\n1. Binary Integers")
print("\t Integer of binary 0b10 is " + str(0b10))
print("\t Convert string to int." + str(int("496")))

#-----------------------------------Floats-----------------------------------#
print("\n2. Float numbers - Numbers with decimal point")
print("\t" + str(3.125))
print("\tSpeed of light is " + str(3e8))
print("\t" + str(1.6e-5))
print("\tFloat value of integer 7 is " + str(float(7)))
# implicit conversion string to float
print("\tPi value is " + str(float("3.14")))
# Predefined data values in Python: nan(not a number), inf(infinite), -inf(negative infinite)
print("\t This is not a number: " + str(float("nan")))
print("\t This is infinite number: " + str(float("inf")))
print("\t This is negative infinite number: " + str(float("-inf")))
# implicit conversions float + int = float
print("\t This is addition of a float and an integer: " + str(3.5 + 5))

#-----------------------------------None-----------------------------------#
print("\n2. Null - None is Null in python")
print("\tI'm null- " + str(None))
none_num = None
print(none_num is None)