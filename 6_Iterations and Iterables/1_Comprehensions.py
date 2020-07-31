from math import factorial
from math import sqrt

print("Comprehensions are syntax for describing lists, sets, dictionaries")

print("\t1. List comprehensions. Syntax: [expr(item) for item in iterable]")
temp_string = "Sandeep Laxman Dhamale".split()
print("\tComprehension for counting length of each word: [len(word) for word in temp_string] " + str([len(word) for word in temp_string]))

print("\t2. Sets comprehensions. It eliminates duplicates. Syntax: {expr(item) for item in iterable}")
s={"I am cat with super colors"}
#s_list = s.split()
print("\tComprehension for counting length of each word: " + str({len(word) for word in s}))

print("\t3. Dictionary comprehensions.")
country_capitals = {"India" : "Delhi",
                    "USA" : "Washington",
                    "China" : "Beijing"}
print("\tReversing country_capitals list using comprehensions: ")
capitals_country = {capital:country for country, capital in country_capitals.items()}
from pprint import pprint as pp
pp(capitals_country)

print("\t4. Filtering comprehensions.")
def is_even(arg_number):
    if(arg_number %2==0):
        return True
    else:
        return False
print("\tEven numbers upto 50: " +str([num for num in range(50) if is_even(num)]))

print("\n5. iterable and iterator. iterator = iter(iterable)")
print("\tGet values from iterator using next()")
iterable = ['Spring', 'Autumn', 'Winter', 'Summer']
iterator = iter(iterable)
iterator_next_value = next(iterator)
print("\tNext value = " + iterator_next_value)
iterator_next_value = next(iterator)
print("\tNext value = " + iterator_next_value)
iterator_next_value = next(iterator)
print("\tNext value = " + iterator_next_value)
iterator_next_value = next(iterator)
print("\tNext value = " + iterator_next_value)

print("\nGenerator functions. Must include atleast one yield statement.")
def generator_function():
    yield 1
    yield 2
    yield 3
gf=generator_function()
print("\tgf1 = " + str(gf))
print("\tNext value = " + str(next(gf)))
print("\tNext value = " + str(next(gf)))
print("\tNext value = " + str(next(gf)))