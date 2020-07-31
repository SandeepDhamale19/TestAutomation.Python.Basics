#-----------------------------------Boolean Conversions---------------------------------------------#
# only numbers 0 and 1 can be used for converting to boolean
# Anything else than 0 is converted to true. 0- False, others - True

# num to bool
num_true =1
num_false = 0

bl_true = bool(num_true)
bl_false = bool(num_false)

print("\nNumber to Boolean Conversion")
print("\tNumber: " + str(num_true) + " is boolean: " + str(bl_true))
print("\tNumber: " + str(num_false) + " is boolean: " + str(bl_false))

# bool to num
print("\nBoolean to Number Conversion")
print("\tBoolean: " + str(bl_true) + " is number: " + str(int(bl_true)))
print("\tBoolean: " + str(bl_false) + " is number: " + str(int(bl_false)))

# float to num
num_true_flt = 1.0
num_false_flt = 0.0

bl_true = bool(num_true_flt)
bl_false = bool(num_false_flt)

print("\nFloat to Boolean Conversion")
print("\tNumber: " + str(num_true_flt) + " is boolean: " + str(bl_true))
print("\tNumber: " + str(num_false_flt) + " is boolean: " + str(bl_false))

# String to boolean
#Any Empty string is boolean false
#Any non-empty string is boolean true
empty_str = ""
non_empty_str = "Sandeep"
print("\nString to Boolean Conversion")
print("\tString: " + empty_str + " is boolean: " + str(bool(empty_str)))
print("\tString: " + non_empty_str + " is boolean: " + str(bool(non_empty_str)))

#-----------------------------------String Conversions---------------------------------------------#
# String to Numbers
my_age = "28"
my_birth_year = 1992
current_year = int(my_age) + my_birth_year

print("\nNumber to strings Conversion")
print("\tSum of my age an dob is year:" + str(current_year))

#-----------------------------------Number Conversions---------------------------------------------#
# Number to String
my_f_name = "Sandeep"
my_age = 28

print("\nString to Number Conversion")
print("\tMy name is: " + my_f_name + " and my age is: " + str(my_age))
#print("My name is: " + my_f_name + " and my age is: " + my_age) # Error due to type conversion for my_age
