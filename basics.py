import math

def secondDegree(a=0, b=0, c=0):
	if(a==0):
		return c/b

	disc = (b**2)-(4*a*c)
	if(disc > 0):
		s1 = ((-1*b)+math.sqrt(disc))/(2*a)
		s2 = ((-1*b)-math.sqrt(disc))/(2*a)
		return s1, s2
	if(disc == 0):
		return (-1*b)/(2*a)
	else:
		raise Exception("invalid domain")

def sidePos(a, b):
    sidepos = (sol1 + sol2)/2
    side = (sidepos**2*a)+(sidepos*b)+c


print(secondDegree(1, 2, -2))