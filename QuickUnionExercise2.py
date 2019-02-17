# Union-find with specific canonical element. Add a method find() to the union-find data type so that
# find(i) returns the largest element in the connected component containing ii. The operations,
# union(), connected(), and find() should all take logarithmic time
# or better.
#
# For example, if one of the connected components is {1,2,6,9}, then the find()
# method should return 9 for each of the four elements in the connected components.

import numpy as np


class QuickUnion:
    def __init__(self, size):
        self.id = np.arange(0, size, 1)
        self.biggest = np.copy(self.id)

    def root(self, i):
        while i != self.id[i]:
            # Make every other node in path point to its grandparent to halve path length
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, first, last):
        return self.root(first) == self.root(last)

    def union(self, first, last):
        first_root = self.root(first)
        last_root = self.root(last)
        self.id[first_root] = self.id[last_root]
        if first_root > last_root:
            self.biggest[last_root] = first_root
        else:
            self.biggest[first_root] = last_root

    def find(self, i):
        while i != self.biggest[i]:
            i = self.biggest[i]
        return i


unions = QuickUnion(10)
unions.union(1, 2)
unions.union(1, 9)
unions.union(2, 6)

unions.union(5, 3)

print(unions.find(1))
print(unions.find(2))

print(unions.find(3))
print(unions.find(5))

