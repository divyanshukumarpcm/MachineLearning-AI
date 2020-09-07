import numpy
import matplotlib

def gd(x,y):
    mc=bc=0
    n=len(y)
    lr=0.00000001
    
    for i in range(10):
        yp=mc*x+bc
        md=-(2/n)*sum(x*(y-yp))
        bd=-(2/n)*sum(y-yp)
        mc=mc+lr*md
        bc=bc+lr*bd
        cost=(1/n)*sum(val**2 for val in (y-yp))
        print("m=",mc,"     c=",bc,   "     iteration=",i,"     cost=",cost)
    

y=numpy.array([92,56,88,70,80,49,65,35,66,67])
x=numpy.array([98,68,81,80,83,52,66,30,68,73])
gd(x,y)
#REMEMBER TO PRINT COST