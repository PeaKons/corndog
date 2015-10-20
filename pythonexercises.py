# python learning exercises 

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Functions
def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
		diff = d - b
		if diff < 0:
			diff
			diff *= -1
		return diff
		
def divide(q,v):
	return q / v

def remainder(l, z):
	return l % z
	

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff (10, 5): ", abs_diff(10,5)
	print "test abs_diff (5, 10): ", abs_diff(5,10)
	print "test divide(126, 18): ", divide(126, 18)
	print "test rmainder (40, 18): ", remainder(40,18)
	print "test remainder(126, 18): ", remainder(126, 18)
	print "test power(2,3):"

def main():
	main_function()
	main_arithmetic()
	
main()