# Social network connectivity. Given a social network containing n members and a log file containing m timestamps at
# which times pairs of members formed friendships, design an algorithm to determine the earliest time at which all
# members are connected (i.e., every member is a friend of a friend of a friend ... of a friend). Assume that the log
# file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should
# be m log n or better and use extra space proportional to n.
from QuickUnionExercises.QuickUnion import QuickUnion


members = 6  # n
pairs = 7  # m
log = [(0, 1), (1, 2), (2, 3), (4, 3), (0, 1), (0, 3), (0, 5)]  # fully connected at 7th connection


def union_find(members, log):
    relations = QuickUnion(members)
    connections = len(log)
    for i in range(connections):
        relations.union(log[i][0], log[i][1])

        for j in range(members):
            if not relations.connected(j, j + 1):
                break
            if not relations.connected(members - j - 1, members - j - 2):
                break
            return print("{} connections before fully connected".format(i+1))
    return print("Not fully connected")


union_find(members, log)




