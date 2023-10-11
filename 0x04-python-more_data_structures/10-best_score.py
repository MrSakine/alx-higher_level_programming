#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return (None)
    items = [i for (i, _) in a_dictionary.items()]
    return (sorted(items, reverse=True)[0])
