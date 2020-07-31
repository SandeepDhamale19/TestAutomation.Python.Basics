print("\t1. Value equality operator: '='")
print("\t2. Identity id() equality operator: 'is'")

t = 5
print("\t" + str(id(t)))

t += 2
print("\t" + str(t))
print("\t" + str(id(t)))

print("\n3. Assignment operator (=) binds objects to name and not to value")
r = [1, 2, 3]
print("\tr is " + str(r))
s = r  # Here s and r now refers to same object
print("\ts=r")
print("\tHere s and r now refers to same object " + str(s))
print("\nLet's modify and check values.")
s[1] = 4
print("\ts is modified " + str(s))  # s = [1, 4, 3]
print("\tr is also modified " + str(r))  # r = [1, 4, 3] How come r is modified :) ?
print("\tThis is because r and s refers to same object when assignment was done (s=r)")
print("\tCheck equality of values: ")
print("\tr==s? " + str(s == r))
print("\ts==r? " + str(r == s))
print("\tCheck equality of objects: ")
print("\tCheck r is s? " + str(r is s))

print("\n4. Let's check similar example")
p = [1, 2, 3]
q = [1, 2, 3]
print("\tValue of p is " + str(p))
print("\tValue of q is " + str(q))
print("\tHere although p an q are equal they do not refer to same object i.e. they refer to different lists")

print("\tCheck equality of values: ")
print("\tp==q? " + str(q == p))  # true
print("\tq==p? " + str(q == p))  # true
print("\tCheck equality of objects: ")
print("\tCheck p is q? " + str(p is q))  # false

print("\nLet's modify and check values.")
q[1] = 4
print("\tq is modified: " + str(q))  # q is [1,4,3]
print("\tp is not modified: " + str(p))  # p is [1,2,3]

print("\n5. Let's check for functions")
print("A. Replace by identity reference")
f = [1, 2, 3]
print("\tf is " + str(f))
print("\tDefine a function to replace lists")
def replace(g):
    g[1]=4
    print("\tg is " + str(g))

print("\tInvoke replace function to replace value of list f")
replace(f)
print("\tf is " + str(f))

print("B. Replace by value reference")
m = [1, 2, 3]
print("\tm is " + str(m))
print("\tDefine a function to replace lists")

def replace(n):
    n=[1,2,3]
    n[1] = 4
    print("\tn is " + str(n))

print("\tInvoke replace function to replace value of list m")
replace(m)
print("\tm is " + str(m))

print("\n6.Get Object info.")
print("\tGet type of object: "+ str(type(replace)))
print("\tGet attributes of object: "+ str(dir(replace)))
print("\tGet attributes of object: "+ str(dir(replace.__doc__)))