print("Sets are unordered collection of unique elements")
print("Sets are mutable, unordered. Elements in set must be immutable")
print("Example of sets: s= " + str({1,2,3,4,5}))
print("Set constructor: s=set()")
print("Set constrctor can create a set from any iterable series e.g. list")
s=set([11,23,35,47,59, 35])
print("\tSet: " + str(s)) #Note: Unordered!, duplicates are removed automatically
print("\n1. Iterating over sets")
for item in s:
    print("\t" + str(item))

print("\n2. Adding element to sets:")
s.add(55)
print("\ts= " + str(s))
print("\tAdding multiple elements:")
s.update([22,33,44])
print("\ts= " + str(s))

print("\n3. Removing element from sets:")
s.remove(55)
print("\ts= " + str(s))
s.discard(44)
print("\ts= " + str(s))

print("\n4. Making a shallow copy of element s.copy():")
t= s.copy()
print("\tUsing copy: t= " + str(t))
print("\tUsing set constructor: u= " + str(set(s)))

#By role
set_programmers={'Nadim', 'Harshal', 'Robert', 'Gulab'}
set_QA={'Sandeep', 'Shubhangi', 'Melissa'}
set_DevOps={'Harish', 'Rose'}

#By project
set_GPD={'Nadim', 'Shubhangi', 'Harish'}
set_Cyber={'Harshal', 'Sandeep', 'Rose'}

#By Teams
set_RnA={'Nadim','Shubhangi', 'Sandeep'}
set_CFT={'Melissa', 'Sandeep'}

#By Function
set_Change={'Nadim','Shubhangi', 'Melissa'}
set_Run={'Sandeep', 'Gulab'}

#By Geography
set_Mumbai={'Nadim','Shubhangi', 'Sandeep', 'Gulab', 'Harish'}
set_London={'Robert', 'Rose'}
set_Honkong={'Melissa'}

print("\tList of employees working for RnA OR in Mumbai (Union): ")
set_RnA_OR_Mumbai = set_RnA.union(set_Mumbai)
print("\t" + str(set_RnA_OR_Mumbai))

print("\tList of employees working in Mumbai AND for RnA (intersection): ")
set_RnA_AND_Mumbai = set_RnA.intersection(set_Mumbai)
print("\t" + str(set_RnA_AND_Mumbai))

print("\tList of employees working in Mumbai And not in RnA (difference): ")
set_RnA_AND_NOT_IN_Mumbai = set_Mumbai.difference(set_RnA)
print("\t" + str(set_RnA_AND_NOT_IN_Mumbai))

print("\tList of employees working in RnA And in Change but not in both (symmetric difference): ")
set_RnA_AND_Mumbai_NOT_BOTH = set_RnA.symmetric_difference(set_Change)
print("\t" + str(set_RnA_AND_Mumbai_NOT_BOTH))

print("\tCheck for subset: ")
print("\t" + str(set_Run.issubset(set_Mumbai)))
print("\t" + str(set_Run.issubset(set_London)))

print("\tCheck for nothing common between sets: ")
print("\t" + str(set_Mumbai.isdisjoint(set_London)))
