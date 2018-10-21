from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    # split strings in lines a and b with \n as delimiter and return it in an array
    list_splitLinesA = a.splitlines()
    list_splitLinesB = b.splitlines()
    return(similarLines(list_splitLinesA, list_splitLinesB))

def  similarLines(list_splitLinesA, list_splitLinesB):
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
    return []
