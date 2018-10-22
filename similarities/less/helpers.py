from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    # TODO
    # split strings in lines a and b with \n as delimiter and return it in an array
    list_splitLinesA = a.splitlines()
    list_splitLinesB = b.splitlines()
    return(similarLines(list_splitLinesA, list_splitLinesB))


def similarLines(list_splitLinesA, list_splitLinesB):
    return list(set(list_splitLinesA) & set(list_splitLinesB))


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    # sent_tokenize splits a sentence ending with a period and returns it in a list
    listA = sent_tokenize(a)
    listB = sent_tokenize(b)
    return(similarSentences(listA, listB))
# function to return similar sentences


def similarSentences(listA, listB):
    return list(set(listA) & set(listB))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return compare_lists(tokenize(a, n), tokenize(b, n))

# function to substring strings a and b with a given value of n and append it to a list if no duplicates are found


def tokenize(s, n):
    result = []
    for i in range(len(s)-n+1):
        token = s[i:i+n]
        if not token in result:
            result.append(token)
    return result


# function to compare substring lists and return similar substrings
def compare_lists(list1, list2):
    result = []
    for la in list1:
        for lb in list2:
            if la == lb and la not in result:
                result.append(la)

    return result

