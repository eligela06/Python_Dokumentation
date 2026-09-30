raw_edges = [("A", "B"), ("B", "A"), ("B", "C"), ("C", "D"), ("A", "B"), ("D", "C")]

edges = {frozenset(edge) for edge in raw_edges}

print("Distinct connections:", len(edges))
print('Edge "A-B" exists:', frozenset(("A", "B")) in edges)
print('Edge "X-Y" exists:', frozenset(("X", "Y")) in edges)