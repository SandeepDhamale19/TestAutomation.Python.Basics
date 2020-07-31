print("Class. Syntax: class MyClassName:")
print("\tInteger type: " + str(type(5)))
print("\tString type: " + str(type("Python")))
print("\tList type: " + str(type([1,2,3])))
print("\tSet type: " + str(type({1, 2, 3})))
print("\tTuple type: " + str(type((1, 2, 3))))
print("\tDictionary type: " + str(type({'a':1, 'b': 2, 'c':3})))
print("\tGenerator type: " + str(type(x*x for x in [2,4,6])))

class MyFirstPython:
    pass

print("\n1. Class: " + str(MyFirstPython))
c = MyFirstPython()
print("\t1. Type of Class: " + str(type(c)))
