from sample1 import *
from sample2 import div
while(True):
    try:
        a=int(input("enter value of a: "))
        b=int(input("enter value of b: "))
        res=div(a,b)
    except KvrDivisionError:
        print('dont enter zero for den....')
    except ValueError:
        print('dont enter alnums,strs,and symbols')
    else:
        print("div({},{})={}".format(a,b,res))
