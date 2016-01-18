def myMod(largenumber,n):
	#Divide the number by the n in mod(n)
	x = (float(largenumber) / float(n))

	#Get the decimal part and times by n
	answer = ((x - int(x)) * n)

	#Round up
	answer = int(round(answer))
	return(answer)

def defaultpythonMod(largenumber,n):
	return( largenumber % n)


def checker(largenumber,n):

	test1 = pythonMod(largenumber,n)
	test2 = myMod(largenumber,n)

	if (test1 == test2):
		print("Works fine(Results: %d, %d)"  % (test1,test2)  )

	else:
		print("Something has gone wrong")

checker(590,3)
#checker()