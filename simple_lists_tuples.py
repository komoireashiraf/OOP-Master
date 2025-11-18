# Tiny demo: lists vs tuples (very short)

lst = [1, 2, 3]
tup = (1, 2, 3)

# lists are mutable
lst.append(4)

# tuples are immutable - this would raise AttributeError
try:
    tup.append(4)
except AttributeError:
    pass

print("list:", lst)
print("tuple:", tup)

# convert list -> tuple when you need immutability
tup2 = tuple(lst)
print("tuple after convert:", tup2)
