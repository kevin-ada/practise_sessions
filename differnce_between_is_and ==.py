# The expression == acts as an equality opeator
# The expression 'is' acts as an identity operator

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4, 5, 6, 7]

if l1 is l2:
    print(True)
else:
    print(False)


print(id(l1) == id(l2))
