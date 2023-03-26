#create an empty set 
s = set()

#add element to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4)
s.add(3)

print(s)

#to remove an elemnt form the set 
s.remove(4)
print(s)

#set lenght
print(f"This set has {len(s)} elements.")