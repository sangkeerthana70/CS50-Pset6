def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    # split strings in lines a and b with \n as delimiter and return it in an array
    list_splitLinesA = a.splitlines()
    list_splitLinesB = b.splitlines()
    return(intersection(list_splitLinesA, list_splitLinesB))

def  intersection(list_splitLinesA, list_splitLinesB):
    return list(set(list_splitLinesA) & set(list_splitLinesB))

def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    return []


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
