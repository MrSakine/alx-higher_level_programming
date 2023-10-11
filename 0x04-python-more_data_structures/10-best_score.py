#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return (None)
    items = [[i, j] for (i, j) in a_dictionary.items()]
    bestScore = items[0][1] if len(items) > 0 else 0
    name = None
    for i in items:
        n = i[1]
        if (n > bestScore):
            bestScore = n
            name = i[0]
    return (name)
