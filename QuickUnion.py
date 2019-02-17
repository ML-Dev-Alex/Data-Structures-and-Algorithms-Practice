import numpy as np


class QuickUnion:
    def __init__(self, size):
        self.id = np.arange(0, size, 1)

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
