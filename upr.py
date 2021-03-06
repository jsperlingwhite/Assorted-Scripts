# trying to recreate the old upr.py
# hopefully this is more or less right
# (also more modular, iirc)
# i forgot how to code so this may look weird but it works

def upr(c,a,y,t,i):
	alpha = ((c/a) - .3) * 5
	beta = ((y/a) - 3) * .25
	gamma = (t/a) * 20
	delta = 2.375 - (i/a) * 25
	upr = ((alpha + beta + gamma + delta) / 6) * 100
	return upr

def spr(c,a,y,t,i):
	alpha = max(0,min(2.375,((c/a) - .3) * 5))
	beta = max(0,min(2.375,((y/a) - 3) * .25))
	gamma = max(0,min(2.375,(t/a) * 20))
	delta = max(0,min(2.375,2.375 - (i/a) * 25))
	spr = ((alpha + beta + gamma + delta) / 6) * 100
	return spr

while True:
	c = int(input("completions > "))
	a = int(input("attempts    > "))
	y = int(input("yards       > "))
	t = int(input("tds         > "))
	i = int(input("ints        > "))
	print("upr is", upr(c,a,y,t,i))
	print("standard pr would be", spr(c,a,y,t,i))
