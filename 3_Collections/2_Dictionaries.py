#Map Key to values
#Syntax: {key1:value1, key2:value2,...}
#Keys must be unique and immutable
#Values can be duplicate and mutable

#-----------------------------------Dictionaries-----------------------------------#
dict_Employees = {10001:"Sandeep", 10002:"Vinod", 10003:"Jack"}
print("\n1. Lists of Employees")
print("\tList of Employees: " + str(dict_Employees))

#Get value based on key
print("\n2. Get value based on key")
print("\tEmployee name with code 10001: " + dict_Employees[10001])

#Update value based on key
dict_Employees[10003] = "Rob"
print("\n3. Update value based on key")
print("\tList of Employees: " + str(dict_Employees))

#Add values to list
#If key is not present within dict then new entry is made
dict_Employees[10004]= "Sara"
print("\n4. Add values to list")
print("\tList of Employees: " + str(dict_Employees))

# Retrieve List using for loop
print("\n5. Retrieve List using for loop")
for employee in dict_Employees:
    print("\t", employee, dict_Employees[employee])

# Convert tuples to Dictionary
print("\n6. Convert tuples to Dictionary")
t = [("f_name", "Sandeep"), ("m_name", "Laxman"), ("l_name", "Dhamale")]
d= dict(t)
print("\td= " + str(d))

# Creating dictionary from keyword arguments
print("\n7. Creating dictionary from keyword arguments")
d = dict(a='alpha', b='bravo', c='charlie', d='delta')
print("\td=" + str(d))

# Copying dictionary
print("\n8. Copying dictionary")
e = d.copy()
print("\te=" + str(e))
f=dict(d)
print("\tf=" + str(f))

#Adding entries from another dictionary dict.update()
print("\n9. Adding entries from another dictionary dict.update()")
g= dict(e='even', f='fruits')
g.update(d)
print("\tg=" + str(g))

print("\tIf source and target dictionaries have same keys then source key values are replaced with target values")
h= dict(d='dog', e='even', f='fruits')
h.update(d)
print("\th=" + str(h))

# Iterating over dictionaries
print("\n10. Iterating over dictionaries - key and values")
for key in d:
    print(f"\t{key}:{d[key]}")
print("\tIterating over dictionaries - values")
for value in d.values():
    print("\t" + str(value))
print("\tIterating over dictionaries - keys")
for key in d.keys():
    print("\t" + str(key))
print("\tIterating over dictionaries - keys and values")
for key, value in d.items():
    print(f"\t{key}:{value}")

# Verify key present in Dictionary
print("\n11. Verify key present in Dictionary")
is_key_present = 'c' in d
print("\t d = " + str(d))
print("\tKey present in dictionary: " + str(is_key_present))

# Delete key
print("\n11. Delete key from Dictionary")
i = dict(d)
del i['c']
print("\t i = " + str(i))
print("\t d = " + str(d))

# Modifying dictionary values
d['d'] += 'force'
print("\n12. Modifying dictionary values")
print("\t d = " + str(d))

# Adding dictionary values
d['e'] = 'ether'
print("\n13. Adding dictionary values")
print("\t d = " + str(d))