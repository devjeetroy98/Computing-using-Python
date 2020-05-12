# Data Structure using Python
l1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
l2 = [98, 99, 100]
# .append()
l1.append(l2)
print(l1)
# .extend()
l1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
l1.extend(l2)
print(l1)
# .insert()
l1.insert(0, 'Start')
print(l1)
# .remove()
l1.remove(100)
print(l1)
# l1.remove(100) throws a value error
# .pop()
l1.pop()
print(l1)
l1.pop(8)
print(l1)
