import random
from fractions import gcd

def RSA(p ,q):

	n = p * q
	fiN = (p - 1) * (q - 1)

	i = 2
	possiblePublicKeys = []

	while(i < fiN):

		if ((gcd(i, fiN) == 1)):
			possiblePublicKeys.append(i)
		i = i + 1

	#print possiblePublicKeys
	e = possiblePublicKeys[random.randrange(len(possiblePublicKeys) - 1) ]
	print("e = %d") % e

	d = 1
	while(e * d % fiN != 1):
	 	d = d + 1

	print("d = %d") % d

	plaintext = 1234
	print("So we encrypt: %d " % plaintext)

	ciphertextmessage = encryption(e,n, plaintext)

	print("So the coded message is: " + str(ciphertextmessage))
	print("Decoded message is " + str(decryption(d,n, ciphertextmessage)) )

def encryption(e, n , plaintext):

	ciphertext =(plaintext ** e) % n
	return(ciphertext)

def decryption(d, n, ciphertext):

	plaintext =(ciphertext ** d) % n
	print ("dM: %d"  % (ciphertext))
	return(plaintext)

RSA(1223,1259)

