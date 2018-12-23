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
