def search(lst):
    """
    Function that searchs for value in the nested list
    :param lst:
    :yield: either a value if 'i' is not a list or a tuple, otherwise calls the search generator function again
    """
    for i in lst:
        if i is not None:
            if not isinstance(i, (list, tuple)):
                yield i
            else:
                yield from search(i)


def flatten(array):
    """
    Function that accepts an arbitrarily-deep nested list-like structure and
    returns a flattened structure without any None.
    :param array: nested list
    :return: a single list
    """
    return list(search(array))
