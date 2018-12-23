''' mutable : list, dict, bytearray, set
    immutable : numbers, tuple, str, frozenset, bool'''
    
#Some examples:

a = 4 
print(id(a))   #1584027968

a += 1
print(id(a))   #1584927984

#As you see, id changed

a = True
print(id(a))   #1583846512

a = False
print(id(a))   #1583846528

#Id changed too


a = [1, 2, 3]    #list
print(id(a))   #5540960

a.append(4)     # .append(argument) appends argument to end of list. 
print(id(a))   #5540960 


# All id at your computer will be different from mine


# Some differences in functions
# Mutable objects are called by reference in functions with access to original object
# Immutable objects are called by value in functions

def updateList(my_list):
    my_list.append(10)
    
n = [1, 2, 3]
print(id(n))    # 9543512

updateList(n)
print(n)           # [1, 2, 3, 10]
print(id(n))    # 9543512

def updateNumber(n):
    n += 10
    
b = 10
updateNumber(10)
print(b)   # 10

# Warning!
# Not all immutable objects actually immutable
# Some example with tuple

t = (1, 2, 3, [4, 5])
t[3].append(6)
print(t)    # (1, 2, 3, [4, 5, 6])

# Something about type
# type(object) return type of object :)

a = 3
b = .6
t = (1, 2)

for i in (a, b, t):
    print(type(i))  

# If you don't understand smth here, check this : https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747
