#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp = [i for i in my_list]
    return (list(map(lambda x: x if x != search else replace, temp)))
