def seanMod(largenumber,n):
	#Divide the number by the n in mod(n)
	x = (float(largenumber) / float(n))

	#Get the decimal part and times by n
	answer = ((x - int(x)) * n)

	#Round up
	answer = int(round(answer))
	return(answer)

def pythonMod(largenumber,n):
	return( largenumber % n)


def checker(largenumber,n):

	test1 = pythonMod(largenumber,n)
	test2 = seanMod(largenumber,n)

	if (test1 == test2):
		print("Good code(Results: %d, %d)"  % (test1,test2)  )

	else:
		print("try harder Sean")

checker(590,3)
#checker()