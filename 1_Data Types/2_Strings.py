import math
#-----------------------------------Normal string-----------------------------------#
print("1. Print string")
print("\tHello World!")
print("\tStrings are immutable. You can not modify them in place.")

#-----------------------------------String with Quotes-----------------------------------#
# String with Quotes
print("\n2. String with Quotes")
print("\t\"Sandeep Dhamale\"")

#-----------------------------------String Concatenation-----------------------------------#
# String Concatenation ('+' operator)
my_f_name= "Sandeep"
my_m_name= "Laxman"
my_l_name = "Dhamale"
print("\n3. String Concatenation ('+' operator)")
print("\tMy name is: " + my_f_name + " " + my_l_name)
print("\tMy name is: " + "\"" + my_f_name + " " + my_l_name + "\"")

my_name = "Sandeep"
my_name += " Laxman"
my_name += " Dhamale"
print("\tMy name is: " + my_name)

#-----------------------------------String Join-----------------------------------#
print("\n3a. String Join <seperator>.join")
seperator = " "
my_name = seperator.join([my_f_name, my_m_name, my_l_name])
print("\tMy name is: " + my_name)
#-----------------------------------String Join-----------------------------------#
print("\n3b. String split string.split(seperator)")
lst_my_name = my_name.split(seperator)
print("\t" + str(lst_my_name))
for my_name_attributes in lst_my_name:
    print("\t"+ my_name_attributes)

# -----------------------------------String Partition-----------------------------------#
print("\n3c. String partition by a word within string string.split('word'')")
split_word = "play"
split_string = "unplayable"
list_seperated_words = split_string.partition(split_word)
print("\tList of sub strings: " + str(list_seperated_words))
print("\tAssigning partitioned substrings to variables")
departure, seperator, arrival = "Mumbai:Delhi".partition(":")
print("\tDepature: " + departure + ", Arrival: " + arrival)
#-----------------------------------Case conversion-----------------------------------#
# Case conversion [text.upper(), text.lower()]
print("\n4. Case conversion  [text.upper(), text.lower()]")
#f_name = input("\tPlease enter your first name: ")
f_name = "Sandeep Dhamale"
print("\tYour name in upper case is " + f_name.upper())
print("\tYour name in lower case is " + f_name.lower())

#-----------------------------------String Length-----------------------------------#
# Length [len(text)]
print("\n5. Length of string [len(text)]")
#f_name = input("\tPlease enter your first name: ")
print("\tYour name is " + str(len(f_name)) + " characters long.")

#-----------------------------------Character Count-----------------------------------#
# Count [text.count("<char>"), text.count("<subText>")]
char_to_verify = "a"
temp_str = "I am a programmer."
subString_to_verify = "am"

print("\n6. Count character occurance in a string [text.count'<char>')]")
print("\tCharacter '"+char_to_verify + "' occured " + str(f_name.count(char_to_verify)) + " times within string " + f_name)
print("\tSubstring 'am' occured " + str(temp_str.count(subString_to_verify)) + " times within string " + temp_str)

#-----------------------------------Starts With/ Ends With-----------------------------------#
# Starts With[text.startswith(subText)]
print("\n7. Starts With[text.startswith(subText)]")

starts_with_str = "Bill"
temp_str = "Bill Cosby just got a huge legal bill"
if(temp_str.lower().startswith(starts_with_str.lower())):
    print("\t" + temp_str + " starts with " + starts_with_str)
else:
    print("\t" + temp_str + " does not start with " + starts_with_str)

# Ends With[text.endswith(subText)]
print("\n8. Ends With[text.endswith(subText)]")

ends_with_str = "Bill"
temp_str = "Bill Cosby just got a huge legal bill"
if(temp_str.lower().endswith(ends_with_str.lower())):
    print("\t" + temp_str + " ends with " + ends_with_str)
else:
    print("\t" + temp_str + " does not end with " + ends_with_str)

#-----------------------------------Find Substring in a String-----------------------------------#
# Find[text.find(subText)] - Find index of Char/ String
# First char is counted as position 0
print("\n9. Find[text.find(subText)] - Find index of Char/ String")

find_str = "is"
temp_str = "This is not his wish"
print("\t" + str(temp_str.lower().find(find_str.lower())))
if(temp_str.lower().find(find_str.lower())):
    print("\t" + temp_str + " contains '" + find_str + "' at position " + str(temp_str.lower().find(find_str.lower())))
else:
    print("\t" + temp_str + " does not contain " + find_str)

#-----------------------------------Substring at position-----------------------------------#
# Substring at index
print("\n10. Substring[text[index]] - Find Char/ String from position[index]")

index_start_int = 8
index_end_int = 11
temp_str = "This is not his wish"
print("\tSubstring at position " + str(index_start_int) + " is '" + temp_str[index_start_int] + "'")
print("\tSubstring at position " + str(index_start_int) + " to position " + str(index_end_int) + " is '" + temp_str[index_start_int:index_end_int] + "'")
print("\tSubstring from position " + str(index_start_int) + " is '" + temp_str[index_start_int:] + "'")
print("\tSubstring till position " + str(index_end_int) + " is '" + temp_str[:index_end_int] + "'")

# RFind[text.find(subText)] (reverse find - find index of Char/ String last occurrence)
print("\n11.rfind[text.find(subText)] - (reverse find - find last occurrence of char/ string)")

find_str = "is"
temp_str = "This is not his wish"
print("\tThe text '" + find_str + "' is at position " + str(temp_str.lower().rfind(find_str.lower())) + " in string '" + temp_str + "'")
if temp_str.lower().rfind(find_str.lower()):
    print("\t" + temp_str + " contains '" + find_str + "' at position " + str(temp_str.lower().rfind(find_str.lower())))
else:
    print("\t" + temp_str + " does not contain " + find_str)

#-----------------------------------Replace-----------------------------------#
# Replace [text.replace(old_subText, new_subText)]
print("\n12. Replace [text.replace(old_subText, new_subText)]")
temp_str = "My name is Lakhan"
old_substr = "Lakhan"
new_substr = "Sandeep"
print("\t Old text: '" + temp_str + "' is now :'" + temp_str.replace(old_substr, new_substr) + "'")

#-----------------------------------Multiline strings-----------------------------------#
# Multiline Strings
# Using 3 double quates
print("\n13. Multiline Strings: Using 3 double quates")
print("""\tThis is first line.
\tThis is second line.
\tThis is third line.""")

# Using Escape sequence: \n
print('\n14. Multiline Strings: Using Escape sequence \\n')
print("\tThis is first line.\n\tThis is second line.\n\tThis is third line.""")

#-----------------------------------Using Escape Sequences-----------------------------------#
print("\n15. Using Escape sequence '\\'")
print("\tThis is a double quote \" in a string")
print("\tThis is a single quote \' in a string")
print("\tThis is a double quote \" and a single quote \' in a string")
print("""\tThis is a new line escape sequence \\n
\tThis is a tab escape sequence \\t
\tThis is a back slash escape sequence \\
\tThis is a carriage return escape sequence \\r""")

#-----------------------------------File paths-----------------------------------#
print("\n16. File Paths: r")
filePath = r'C:\Sandeep\Python\MyFirstPythonProject\MyFirstPythonScript.py'
print(filePath)

#-----------------------------------String Fotmatting- Interpolation-----------------------------------#
print("\n17. Formatting strings with positional and keyowrd arguments")
print(("\tPositional arguments:"))
print("\t{0} is my first name. {1} is my last name.".format("Sandeep", "Dhamale"))
print(("\tKeyword arguments:"))
print("\t{my_f_name} is my first name. {my_l_name} is my last name.".format(my_f_name = "Sandeep", my_l_name = "Dhamale"))
print(("\tKeyword arguments with diferent positions:"))
print("\t{my_l_name} is my last name. {my_f_name} is my first name.".format(my_f_name = "Sandeep", my_l_name = "Dhamale"))
print(("\tKeyword arguments with tuples:"))

print("\tOlympic medal tally position Rank1={medal_tally[0]}, Rank2={medal_tally[1]}, "
      "Rank3={medal_tally[2]}".format(medal_tally = ("US", "China", "France")))
#-----------------------------------String literals-Interpolation: f strings-----------------------------------#
print("\n18.f-strings are represented by f'string' and are used to evaluate expression at run time directly within string.")
temp_value = 4*20
print("\tValue of expression is: " + str(f'{temp_value}'))
print(f"\tMath constants: pi={math.pi}, e={math.e}")

#-----------------------------------Help-----------------------------------#
print("\n Help function for str")
temp_str = "Sandeep Dhamale"
#help(str)
print("\tReturn a capitalized version of the string: " + temp_str.capitalize())
print("\tReturn a version of the string suitable for caseless comparisons: " + temp_str.casefold())
print("\tReturn the number of non-overlapping occurrences of substring in string S[start:end]: " + str(temp_str.count('Sa')))