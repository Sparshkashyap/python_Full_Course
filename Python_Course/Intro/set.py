
"""
set is mutable 
frozenset is immutable

"""

# unique_set = {1,2,2,2,3,3,4,5,6,6,6,6,7}
# unique_set.add(10)
# unique_set.remove(1)
# print(unique_set)


unique_frozenset = frozenset({1,1,2,3,4,5,6,7,8,1,2})
unique_frozenset.add(15)
print(unique_frozenset)
