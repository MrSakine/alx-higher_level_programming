#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = copy_tuple(tuple_a)
    tuple_b = copy_tuple(tuple_b)

    return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))


def copy_tuple(value={}):
    copy = [i for i in value]
    tmp = []

    if (len(copy) == 0):
        return (0, 0)
    elif (len(copy) > 2):
        return tuple(copy[:2])
    else:
        for i in range(2):
            try:
                if (copy[i]):
                    tmp.append(copy[i])
                pass
            except Exception:
                tmp.append(0)

        return tuple(tmp)
