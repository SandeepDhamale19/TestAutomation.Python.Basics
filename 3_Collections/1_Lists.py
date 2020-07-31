# Lists are sequence of objects
# Mutable
# Lists are represented within square brackets and items are seperated by commas

#-----------------------------------Lists-----------------------------------#
# Lists of Numbers
print("\n1. Lists of Numbers")
print("\t" + str([1,2,3]))

# Lists of Strings
print("\n2. Lists of Strings")
print("\t" + str(["Lemon","Mango","Papaya"]))

list_fruits =["Lemon","Mango","Papaya"]
print("\tMy favorite fruit is " + list_fruits[1])

print("\n3. List operations")
#Replace items within list
list_fruits[2]="Water Melons"
print("\tNew List: " + str(list_fruits))

#Create Empty List
list_Organizations = []
print("\n5. Create empty list")
print("\tList of Organizations: " + str(list_Organizations))

#Add values to list
print("\n5. Add values to list")
list_Organizations.append("Microsoft")
list_Organizations.append("Amazon")
list_Organizations.append("Google")
print("\tAppend List of Organizations: " + str(list_Organizations))

#List of characters within string
print("\tList of characters in  string:" + str(list("Sandeep Dhamale")))

# Retrieve List using for loop
print("\n6. Retrieve List using for loop")
for organization in list_Organizations:
    print("\t" + organization)

# Get specific elements within list: Slicing
print("\n7. Get specific elements within list: Slicing")
list_numbers = [1,2,3,4,5]
sub_list_numbers = list_numbers[1:3]
print("\tSub list: " +  str(sub_list_numbers))
print("\tLast element in list: " +  str(list_numbers[-1]))
print("\tGet all elements in list except first and lasr: " +  str(list_numbers[1:-1]))
print("\tElements from index 2 in list: " +  str(list_numbers[2:]))
print("\tElements till index 4 in list: " +  str(list_numbers[:4]))

#Copying Lists to other list - Shallow copy
print("\n8. Copying Lists to other list")
list_numbers_direct = list_numbers
print("\tUsing assignment. Is list_numbers_direct is list_numbers " + str(list_numbers_direct is list_numbers))

list_numbers_list_values = list_numbers[:]
print("\tUsing assignment. Is list_numbers_list_values is list_numbers " + str(list_numbers_list_values is list_numbers))

list_numbers_copy = list_numbers.copy()
print("\tUsing assignment. Is list_numbers_copy is list_numbers " + str(list_numbers_copy is list_numbers))

list_numbers_list = list(list_numbers)
print("\tUsing assignment. Is list_numbers_list is list_numbers " + str(list_numbers_list is list_numbers))

print("\n9. Note: Although the copies are not equal the objects inside the lists are equal")
list_of_list = [[1,2],[3,4]]
copy_list_of_list = list_of_list[:]
print("\tcopy_list_of_list is list_of_list: " + str(copy_list_of_list is list_of_list))
print("\tcopy_list_of_list[element] is list_of_list[element]: " + str(copy_list_of_list[0] is list_of_list[0]))
print("\tEven if the values are modified e.g. append the list will be same")
list_of_list[0].append('a')
print("\tlist_of_list: " + str(list_of_list))
print("\tcopy_list_of_list: " + str(copy_list_of_list))
print("\tcopy_list_of_list[element] is list_of_list[element]: " + str(copy_list_of_list[0] is list_of_list[0]))

print("\n10.Search in a list: list.index() - Returns the first matched element")
temp_string = "Python is easy scripting language. It is easy to learn and build apps using Python."
temp_string_list = temp_string.split(" ")
print("\tString: " + temp_string)
print("\tString list: " + str(temp_string_list))
print("\tSearch a sub string in string list using list.index(): " + str(temp_string_list.index("scripting")))

print("\n11.Count occurrence of substring in list")
print("\tCount occurrence of substring Python: " + str(temp_string_list.count("easy")))

print("\n12.Remove substring from string list")
del temp_string_list[3]
print("\tA. Remove substring from list using del (by index): " + str(temp_string_list))
print("\tOriginal string is unaffected: " + str(temp_string))

temp_string_list.remove("learn")
print("\tB. Remove substring from list using remove (by value): " + str(temp_string_list))
print("\tOriginal string is unaffected: " + str(temp_string))

print("\n12.Insert a substring in string. list.insert()")
temp_string_list.insert(3, "scripting")
print("\tA. Insert substring to list (at index): " + str(temp_string_list))
print("\tOriginal string is unaffected: " + str(temp_string))

print("\n13.Concatenating lists.")
temp_list_1=[1,2,3]
temp_list_2 = [4,5,6]
temp_list = temp_list_1 + temp_list_2
print("\ta. temp_list = temp_list_1 + temp_list_2 = " + str(temp_list))
temp_list+=temp_list
print("\tb. temp_list += temp_list " + str(temp_list))
temp_list.extend([7,8,9])
print("\tc. temp_list.extend() " + str(temp_list))

print("\n14. Reversing lists.")
temp_list.reverse()
print("Reverse temp list: "+ str(temp_list))

print("\n15. Sorting lists.")
temp_list = [5,55,555]
temp_list.sort()
print("\tSorted list: " + str(temp_list))
temp_list.sort(reverse=True)
print("\tSorted list: " + str(temp_list))
print("\tSorting lists by callable functions (inbuilt) e.g. len using 'key")
temp_string = "I am a software tester."
temp_string_list = temp_string.split()
print("\tString list: " + str(temp_string_list))
temp_string_list.sort(key=len)
print("\tSort by length of each word: " + str(temp_string_list))
temp_number_list=[3,45,12,1,99,44]

print("\n16. Using Sorted (copy of sort) instead of sort. and reversed to avoid modifications in original list.")
x=[4, 9, 2, 1]
y = x
y.sort()
print("\t y= " + str(y))
print("\t x= " + str(x))

x=[4, 9, 2, 1]
print("\t y= " + str(sorted(x)))
print("\t x= " + str(x))
print("\t z= " + str(list(reversed(x))))
print("\t x= " + str(x))
