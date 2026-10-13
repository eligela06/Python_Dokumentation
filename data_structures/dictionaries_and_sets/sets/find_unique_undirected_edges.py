# You are given a list of raw edges, some of which are duplicates or the same edge listed in reverse order:

# raw_edges = [("A", "B"), ("B", "A"), ("B", "C"), ("C", "D"), ("A", "B"), ("D", "C")]

# Build a set of frozenset pairs representing the distinct, order-independent edges. Print the number of distinct connections, then check whether the edge ("A", "B") exists in the set regardless of the order its endpoints are given in (also check that ("X", "Y") does not).


raw_edges = [("A", "B"), ("B", "A"), ("B", "C"), ("C", "D"), ("A", "B"), ("D", "C")]

edges = set()
ab = set(("A","B"))
xy = set(("X", "Y"))
for start, end in raw_edges:
    edges.add(frozenset((start,end)))

print(ab in edges)

print(xy in edges)