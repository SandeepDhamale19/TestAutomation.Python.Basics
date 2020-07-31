# Syntax: if(condition):
# condition: True/False (Note case for conditions)
# statements with indentation after if are part of conditional block
print("\n1. If condition")
if(True):
    print("\tI'm success!")

if(False):
    print("\tNothing will be printed!")

# Use of indentation
print("\n2. Use of indentation")
print("\n\tExample1: True")
if(True):
    print("\t\tI'm 1st statement and part of 'if'")
    print("\t\tI'm 2nd statement and part of 'if'")

print("\tI'm 3rd statement but not part of 'if'")

print("\n\tExample2: False")
if(False):
    print("\t\tI'm 1st statement and part of 'if'")
    print("\t\tI'm 2nd statement and part of 'if'")

print("\tI'm 3rd statement but not part of 'if'")

# Conditional Operators: <, >, ==, !=, <=, >=
print("\n3. If else condition")
int_num = int(input("\tPlease enter a number: "))
if(int_num < 5):
    print("\tNumber is less than 5!")
else:
    print("\tNumber is greater than or equals 5!")

print("\n4. Multiple conditions")
int_age = int(input("\tPlease enter your age: "))
if(int_age < 5):
    print("\tYou are a kid!")
elif(int_age >= 5 and int_age<18):
    print("\tYou are a child!")
elif(int_age >= 18 and int_age<60):
    print("\tYou are an adult!")
else:
    print("\tYou are a senior person!")