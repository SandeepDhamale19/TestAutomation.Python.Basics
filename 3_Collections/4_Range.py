print("Range are arithmatic progression on integers.")
print("\t" + str(range(5))) #Note values: 0,1,2,3,4 - There is no 5
print("\tList of range" + str(list(range(5))))
print("\tList of range by inteval" + str(list(range(5, 10, 2))))

print("\tWhen one argument is provided its a stop value. e.g. str(range(5) means stop at 5: " + str(range(5)))
print("\tWhen two arguments are provided its start and stop value. e.g. str(range(2, 5) means start at value 2 and stop at value 5: " + str(list(range(2, 5))))
print("\tWhen three arguments are provided its start, stop and step value. e.g. str(range(2, 10, 3) means start at value 2 and stop at value 5 with steps of 3: " + str(list(range(2, 10, 3))))

#-----------------------------------Enumeration-----------------------------------#
print("\nEnumerates constructs an iterable of (index, value). ENumearates are useful when counter is needed along with list")
t=["Rank1", "Rank2", "Rank3", "Rank4", "Rank5"]
for p in enumerate(t):
    print("\t" + str(p))
print("\tMaking use of tuple unpacking: ")
for i,v in enumerate(t):
    print(f"Index {i} : Value {v}")