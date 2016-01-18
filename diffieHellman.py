import random

def diffie(privA,privB,p):

	print("Step 1 : Choose primitive root : typically 2 or 5")
	g = random.randrange(2,6,3)
	print("g is: %d") % g

	print("Step 2 : Choose different private key for Alice and Bob\n")
	print("Alice has private key : %d" % privA)
	print("Bob has private key  : %d" % privB) 
	print("The mod is %d") % p

	gAmodp = g ** privA % p
	gBmodp = g ** privB % p

	print("Sent to Bob : Result of g^A mod n is " + str(gAmodp))
	print("Sent to Alice : Result of g^B mod n is " + str(gBmodp))

	aliceDHK = (gBmodp ** privA) % p
	bobDHK = (gAmodp ** privB) % p

	print("So the decided key is " + str(bobDHK) + ":" + str(aliceDHK))
	print("Actual answer is : %d") % (g ** (privA * privB) % p )

	if (bobDHK == aliceDHK):
		print("Top job done")

	else: 
		print("Fail")


diffie(5,12,29)

#diffie(150098,40785596,12)
 
