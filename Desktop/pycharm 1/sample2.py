from sample1 import *
def div(a,b):
    if (b==0):
        raise KvrDivisionError
    else:
        return a/b