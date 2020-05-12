# Looping or Iteration using Python
for i in range(5):
    print(i, end=' ')

print()

for i in range(15, 26):
    print(i, end=' ')

print()

for i in range(15, 26, 2):
    print(i, end=' ')

print()

mylist = ['a', 'b', 'c', 'd', 'e']
for i in mylist:
    print(i, end=' ')

print()
for ix, val in enumerate(mylist, 0):
    print(ix, "=", val)

