from Custom_Functions import StringsHelpers

print("Tuples: Immutable sequence of arbitrary objects")
t=("Sandeep", 28, 3.14)
print("\n\t1. Example of tuples: t = " + str(t))

print("\n\t2. First object in tuple is t[0] = " + str(t[0]))

print("\n\t3. Number of elements in tuple len(t) = " + str(len(t)))

print("\n\t4. Iterate within tuple using for tuple in tuples: ")
temp_count = 0
for tuple in t:
    temp_count = temp_count + 1
    print("\tItem(" + str(temp_count) + "): " + str(tuple))

print("\n\t5. Add values (concatenation) to tuples t + " + str(t + ("Dhamale", 1.6e-35)))
s = t + ("Dhamale", 1.6e-35)
print("\t" + str(s))

print("\n\t6. Multiply tuples: t * number: " + str(t*3))

nested_tuple= ("Sandeep", 3.14, ("nested tuple string", 15, 1.6e-35))
print("\n\t7. Nested tuples: " + str(nested_tuple))
print("\t8. Get value of tuple element: nested_tuple[2][1]:" + str(nested_tuple[2][0]))
print("\n\t9. Tuples are useful for functions returning multiple values.")
def get_min_max(values):
    return min(values), max(values)
temp_tuple = (1,2,3,4,5)
min_max_values = get_min_max(temp_tuple)
print("\tMinimum and maximum values are: "+ str(min_max_values))

print("\n\t10. Assign returned values to multiple named variables. This is called Tuple unpacking")
min_value, max_value = get_min_max(temp_tuple)
print("\tMinimum value is: " + str(min_value) + ". Maximum value is: " + str(max_value))

print("\n\t11. Assign values to named variables:")
temp_nested_tuple = ("Sandeep", 3.14, ("Dhamale", "ranom string", 1.6e-35))
(my_f_name, pi_value, (my_l_name, random_string, avagadro_number)) = temp_nested_tuple
for item in temp_nested_tuple:
    print("\t" + str(item))
    if(str(type(item))=="<class 'tuple'>"):
        for t in item:
            print("\t\t" + str(t))

print("\n\t12. Swap strings using tuple. 'Sandeep Dhamale' :", StringsHelpers.swap_strings("Sandeep", "Dhamale"))
print("\n\t13. Verify tuple contains value: " + str(5 in (1,2,3,4,5,6,7)))