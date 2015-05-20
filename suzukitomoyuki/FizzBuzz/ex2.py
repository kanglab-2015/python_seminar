if __name__ == "__main__":
	for i in xrange(1,100):
		if i%3 == 0 and i%5 == 0:
			print "fizz buzz"
		elif i%5 == 0:
			print "buzz"
		elif i%3 == 0:
			print "fizz"
		else:
			print i
