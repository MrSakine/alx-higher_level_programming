#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = list([i for i in my_list])

    if ((idx < 0) or (idx >= len(copy))):
        return (copy)
    else:
        copy[idx] = element
        return (copy)
