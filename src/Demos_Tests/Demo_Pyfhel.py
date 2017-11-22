"""Import all the packages useful for the Demo.
#-Pyfhel is useful to generate keys, encrypt and decrypt.
#-PyPtxt is useful to tranform the input vectors into plain text objects that could be encrypted.
#-PyCtxt is useful to tranform the plain text object in PyCtxt object that are encrypted (Cypher texts). PyCtxt can be add, multiply etc with homeomorphic operations."""
from Pyfhel import Pyfhel
from PyPtxt import PyPtxt
from PyCtxt import PyCtxt

"""Other imports useful for the demo."""
from itertools import izip
import itertools
from operator import sub
import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse
import copy

"""Define a parser to parse the arguments given to the program."""
parser = argparse.ArgumentParser()

""" One can specify in the command line of the program either -r or --random (it will be the same to specify -r or --random). This is optional argument. If the user specify it, args.random == True, else args.random == False)"""
parser.add_argument("-r", "--random", help="Perform tests on random vectors.", action="store_true")

""" One can specify in the command line of the program either -f or --fixe (it will be the same to specify -f or --fixe). This is optional argument. If the user specify it, args.fixe == True, else args.fixe == False)"""
parser.add_argument("-f", "--fixe", help="Perform tests on fixed vectors.", action="store_true")

"""One can view a pie chart of the successful tests versus fail tests by adding this option command."""
parser.add_argument("-g", "--graph", help="Display a pie chart of the successful tests versus fail tests..", action="store_true")

"""Parse the arguments given to the program."""
args = parser.parse_args()

"""If the user haven't specify (-r/--random) or (-f/--fixe) in the command line of the program, we run the tests with random vectors of size 5, with the elements between 0 and 1000 folowing an uniform law. Do the same if the user specify only -r/--random."""
if (not args.random and not args.fixe) or (args.random and not args.fixe):
                                                                          """Skip a line, print the title of the Demo, and skip a line again."""
                                                                          print("\n")
                                                                          print("     ************Pyfhel DEMO************")
                                                                          print("\n")

                                                                          """Define two vectors that we will use for the tests (+=, -=, *=, ...)."""
                                                                          v1 = np.random.randint(0, 10, 5).tolist()
                                                                          v2 = np .random.randint(0, 5, 5).tolist()

                                                                          """Define a vector that we will use for the tests (**=2, **=3)."""
                                                                          v_powerSquare = copy.deepcopy(v1)
                                                                          v_powerCube = copy.deepcopy(v1)
                                                                          
                                                                          """Define two vectors that we will use for the tests (+, -, *, ...)."""
                                                                          v12 = copy.deepcopy(v1)
                                                                          v22 = copy.deepcopy(v2)

                                                                          """Define a vector that we will use for the tests (**2, **3)."""
                                                                          v_powerSquare2 = copy.deepcopy(v1)
                                                                          v_powerCube2 = copy.deepcopy(v1)

"""If the user have only specify (-f/--fixe) in the command line of the program, we run the tests with fixe vectors: [1.2.3.4.5], [2,2,2,2,2]."""
if (not args.random and args.fixe): 
                                     """Skip a line, print the title of the Demo, and skip a line again."""
                                     print("\n")
                                     print("     ************Pyfhel DEMO************")
                                     print("\n")

                                     """Define two vectors that we will use for the tests (+=, -=, *=, ...)."""
                                     v1 = [1,2,3,4,5]
                                     v2 = [2,2,2,2,2]

                                     """Define a vector that we will use for the tests (**=2, **=3)."""
                                     v_powerSquare = copy.deepcopy(v1)
                                     v_powerCube = copy.deepcopy(v1)
                                     
                                     """Define two vectors that we will use for the tests (+, -, *, ...)."""
                                     v12 = copy.deepcopy(v1)
                                     v22 = copy.deepcopy(v2)

                                     """Define a vector that we will use for the tests (**2, **3)."""
                                     v_powerSquare2 = copy.deepcopy(v1)
                                     v_powerCube2 = copy.deepcopy(v1)

                                     


"""If the user have specify (-r or --random) and (-f or --fixe) in the command line of the program, display an error."""
if (args.random and args.fixe):
                                 print("Error, you cannot specify -r/--random and -f/--fixe arguments at the same time.")
                                 sys.exit()


"""Define a variable to count the number of succes and the number of fail."""
number_success = 0
number_fail = 0


print("******Definition of the vectors used during the tests******")
print("v1: ", v1)
print("v2: ", v2)


"""Skip a line."""
print("\n")


#Instantiate a Pyfhel object called HE.
HE = Pyfhel()

print("******Generation of the keys for encryption******")

#Create the Key Generator parameters.
KEYGEN_PARAMS={ "p":257,      "r":1,
                "d":1,        "c":2,
                "sec":80,     "w":64,
                "L":10,       "m":-1,
                "R":3,        "s":0,
                "gens":[],    "ords":[]}

"""Print the Key Generator parameters to let the user knows how his vectors will be encrypted."""
print("  Running KeyGen with params:")
print(KEYGEN_PARAMS)

"""Generate the keys that will be use to encrypted the vectors. The generation of the keys uses the Key Generator parameters. Then print a message to inform the user that the key generation has been completed."""
HE.keyGen(KEYGEN_PARAMS)
print("  KeyGen completed")


"""Skip a line."""
print("\n")


"""We will first transform these two vectors in plaintext that could be encrypted, then we'll tranform the plain text of these two vectors in homeomorphic encrypted vector. Then we will add and multiply these two encrypted vectors in an homeomorphic way. Finally, we will decrypted the result of the addition and multiplication of the two encrypted vectors and we verify the result is the same that the addition or multiplication of the two vectors without encryption."""

print("******Homeomorphic encryption of the two vectors used during the tests******")

"""Tranform the two vectors (use to test the operation +=, -=, *=, ...) in plaintext that are objects that could be encrypted."""
ptxt1 = PyPtxt(v1, HE)
ptxt2 = PyPtxt(v2, HE)

"""Tranform the vectors (use to test the operation **=2, **=3) in plaintext that are objects that could be encrypted."""
ptxt_powerSquare = PyPtxt(v_powerSquare, HE)
ptxt_powerCube = PyPtxt(v_powerCube, HE)

"""Tranform the two vectors (use to test the operation +, -, *, ...) in plaintext that are objects that could be encrypted."""
ptxt12 = PyPtxt(v12, HE)
ptxt22 = PyPtxt(v22, HE)

"""Tranform the vectors (use to test the operation **2, **3) in plaintext that are objects that could be encrypted."""
ptxt_powerSquare2 = PyPtxt(v_powerSquare2, HE)
ptxt_powerCube2 = PyPtxt(v_powerCube2, HE)


"""Encrypted the two plaintexts to have two Cypher texts that are encrypted in an homeomorphic way with the key that have been generated before. These two Cypher txt will be use for the test on the homeomorphic operation (+=, -=, *=, ...)"""
ctxt1 = HE.encrypt(ptxt1)
ctxt2 = HE.encrypt(ptxt2)
#ctxt1 = HE.encrypt(ptxt1, fill=1)
#ctxt2 = HE.encrypt(ptxt2, fill=1)


"""Encrypted the plaintexts to have Cypher texts that are encrypted in an homeomorphic way with the key that have been generated before. These Cypher txt will be use for the tests on the homeomorphic operations (**=2, **=3)"""
ctxt_powerSquare = HE.encrypt(ptxt_powerSquare)
ctxt_powerCube = HE.encrypt(ptxt_powerCube)


"""Encrypted the two plaintexts to have two Cypher texts that are encrypted in an homeomorphic way with the key that have been generated before. These two Cypher txt will be use for the test on the homeomorphic operation (+, -, *, ...)"""
ctxt12 = HE.encrypt(ptxt12)
ctxt22 = HE.encrypt(ptxt22)
#ctxt12 = HE.encrypt(ptxt12, fill=1)
#ctxt22 = HE.encrypt(ptxt22, fill=1)


"""Encrypted the plaintexts to have Cypher texts that are encrypted in an homeomorphic way with the key that have been generated before. These Cypher txt will be use for the tests on the homeomorphic operations (**2, **3)"""
ctxt_powerSquare2 = HE.encrypt(ptxt_powerSquare2)
ctxt_powerCube2 = HE.encrypt(ptxt_powerCube2)


print("Encryption of v1...")
print("Encryption of v2...")

print("Encrypted v1: Encrypt(", v1, ")")
print("Encrypted v2: Encrypt(", v2, ")")


"""Skip a line."""
print("\n")


"""Perform homeomorphic operations on the encrypted vectors."""
print("******Test of the homeomorphic operations******")

"""Skip a line."""
print("\n")

"""Perform homeomorphic addition with operator += ."""
print("*** Test of the homeomorphic addition with operator += ***")
print("Encrypted v1: Encrypt(", v1, ")")
print("Encrypted v2: Encrypt(", v2, ")")
print("Performing Encrypt(v1) + Encrypt(v2)...")
print ("test", HE.decrypt(ctxt1))
ctxt1 += ctxt2
"""Decrypt the result of the addition of the two encrypted vectors."""
v_add_v1_v2_decrypt = HE.decrypt(ctxt1)
"""v3 is a list of list ie [[a, b, c,...]], so we want to flatten it to obtain [a, b, c,...]."""
v_add_v1_v2_decrypt_flatten = list(itertools.chain.from_iterable(v_add_v1_v2_decrypt))
"""The user can then verify if the result of the addition of the two encrypted vectors is the same that the addition of the two vectors without encryption."""
print("Decrypt(Encrypt(v1) + Encrypt(v2)) -> ", v_add_v1_v2_decrypt_flatten)
"""Perform the sum on the unencrypted vectors.""" 
v1Plusv2 = map(sum, izip(v1,v2))
print("v3 = v1 + v2 ->", v1Plusv2)
"""If Decrypt(Encrypt(v1) + Encrypt(v2)) equal to v1 + v2, The homeomorphic operation works and so it is a success. Else, it is a fail."""
if v_add_v1_v2_decrypt_flatten == v1Plusv2:
   print("Homeomorphic operation add with operator += is a success: Decrypt(Encrypt(v1) + Encrypt(v2)) equal to v1 + v2.")
   number_success += 1
else:
   print("Homeomorphic operation add with operator += is a fail: Decrypt(Encrypt(v1) + Encrypt(v2)) not equal to v1 + v2.")
   number_fail += 1

"""Skip a line."""
print("\n")


"""Perform homeomorphic substraction with operator -= ."""
print("***Test of the homeomorphic substraction with operator -= ***")
print("Encrypted v3: Encrypt(", v_add_v1_v2_decrypt_flatten, ")")
print("Encrypted v2: Encrypt(", v2, ")")
print("Performing Encrypt(v3) - Encrypt(v2)...")
ctxt1 -= ctxt2
"""Decrypt the result of the substraction of the two encrypted vectors."""
v_minus_v3_v2_decrypt = HE.decrypt(ctxt1)
"""v_add_v1_v2_decrypt is a list of list ie [[a, b, c,...]], so we want to flatten it to obtain [a, b, c,...]."""
v_minus_v3_v2_decrypt_flatten = list(itertools.chain.from_iterable(v_minus_v3_v2_decrypt))
"""The user can then verify if the result of the substraction of the two encrypted vectors is the same that the substraction of the two vectors without encryption."""
print("Decrypt(Encrypt(v3) - Encrypt(v2)) -> ", v_minus_v3_v2_decrypt_flatten)
"""Perform the substraction on the unencrypted vectors."""
v3Minusv2 = map(sub, v_add_v1_v2_decrypt_flatten, v2)
print("v4 = v3 - v2 ->", v3Minusv2)
"""If Decrypt(Encrypt(v3) - Encrypt(v2)) equal to v3 - v2, The homeomorphic operation works and so it is a success. Else, it is a fail."""
if v_minus_v3_v2_decrypt_flatten == v3Minusv2:
   print("Homeomorphic operation substraction with operator -= is a success: Decrypt(Encrypt(v3) - Encrypt(v2)) equal to v3 - v2.")
   number_success += 1
else:
   print("Homeomorphic operation substraction with operation -= is a fail: Decrypt(Encrypt(v3) - Encrypt(v2)) not equal to v3 - v2.")
   number_fail += 1

"""Skip a line."""
print("\n")


"""Perform homeomorphic multiplication with operator *= ."""
print("***Test of the homeomorphic multiplication with operator *= ***")
print("Encrypted v4: Encrypt(", v_minus_v3_v2_decrypt_flatten, ")")
print("Encrypted v2: Encrypt(", v2, ")")
"""ctxt1 contains Encrypt(v4) ie [(Encrypt(v1) + Encrypt(v2))-Encrypt(v2)] ie Encrypt(v1). ctxt2 contains Encrypt(v2). So we perform: Encrypt(v4)*Encrypt(v2) = Encrypt(v1) * Encrypt(v2)"""
print("Performing Encrypt(v4) * Encrypt(v2)...")
ctxt1 *= ctxt2
"""Decrypt the result of the multiplication of the two encrypted vectors."""
v_mult_v4_v2_decrypt = HE.decrypt(ctxt1)
"""v_mult_v4_v2_decrypt is a list of list ie [[a, b, c,...]], so we want to flatten it to obtain [a, b, c,...]."""
v_mult_v4_v2_decrypt_flatten = list(itertools.chain.from_iterable(v_mult_v4_v2_decrypt))
print("Decrypt(Encrypt(v4) * Encrypt(v2)) -> ", v_mult_v4_v2_decrypt_flatten)
"""Perform the multiplication on the unencrypted vectors."""
v4Multv2= [a*b for a,b in izip(v_minus_v3_v2_decrypt_flatten, v2)]
print("v4 * v2 ->", v4Multv2)
"""If Decrypt(Encrypt(v4) * Encrypt(v2)) equal to v4 * v2, The homeomorphic operation works and so it is a success. Else, it is a fail."""
if v_mult_v4_v2_decrypt_flatten == v4Multv2:
   print("Homeomorphic operation mult with operator *= is a success: Decrypt(Encrypt(v4) * Encrypt(v2)) equal to v4 * v2.")
   number_success += 1
else:
   print("Homeomorphic operation mult with operator *= is a fail: Decrypt(Encrypt(v4) * Encrypt(v2)) not equal to v4 * v2.")
   number_fail += 1

"""Skip a line."""
print("\n")


"""Perform homeomorphic Scalar Product with operator %= ."""
print("***Test of the homeomorphic Scalar Product with operator %= ***")
print("Encrypted v5: Encrypt(", v_mult_v4_v2_decrypt_flatten, ")")
print("Encrypted v2: Encrypt(", v2, ")")
"""ctxt1 contains Encrypt(v5) ie [(Encrypt(v1) + Encrypt(v2))-Encrypt(v2)] * Encrypt(v2) ie Encrypt(v1) * Encrypt(v2). ctxt2 contains Encrypt(v2). So we perform: Encrypt(v5) . Encrypt(v2)"""
print("Performing Encrypt(v5) . Encrypt(v2)...")
ctxt1 %= ctxt2
"""Decrypt the result of the Scalar Product of the two encrypted vectors."""
v_scalprod_v5_v2_decrypt = HE.decrypt(ctxt1)
"""v_scalprod_v5_v2_decrypt is a list of list ie [[a, b, c,...]], so we want to flatten it to obtain [a, b, c,...]."""
v_scalprod_v5_v2_decrypt_flatten = list(itertools.chain.from_iterable(v_scalprod_v5_v2_decrypt))
print("Decrypt(Encrypt(v5) . Encrypt(v2)) -> ", v_scalprod_v5_v2_decrypt_flatten)
"""Return the first element of the list or return None if the list is empty."""
v_scalprod_v5_v2_decrypt_flatten_final = next(iter(v_scalprod_v5_v2_decrypt_flatten or []), None)
print("First(Decrypt(Encrypt(v5) . Encrypt(v2))) -> ", v_scalprod_v5_v2_decrypt_flatten_final)
"""Perform the scalar product on the unencrypted vectors."""
v5Dotv2 = sum(i[0] * i[1] for i in zip(v_mult_v4_v2_decrypt_flatten, v2))
print("v5 . v2 ->", v5Dotv2)
"""If First(Decrypt(Encrypt(v5) . Encrypt(v2))) equal to v5 . v2, The homeomorphic operation works and so it is a success. Else, it is a fail."""
if v_scalprod_v5_v2_decrypt_flatten_final == v5Dotv2:
   print("Homeomorphic operation Scalar Product with operator %= is a success: First(Decrypt(Encrypt(v5) . Encrypt(v2))) equal to v5 . v2.")
   number_success += 1
else:
   print("Homeomorphic operation Scalar Product with operator %= is a fail: First(Decrypt(Encrypt(v5) . Encrypt(v2))) not equal to v5 . v2.")
   number_fail += 1


"""Skip a line."""
print("\n")


"""Perform homeomorphic Square Power with the operator **=2 ."""
print("***Test of the homeomorphic Square Power **=2 ***")
print("Encrypted v1: Encrypt(", v1, ")")
"""ctxt_powerSquare contains Encrypt(v1). So we perform: Encrypt(v1) ** 2"""
print("Performing Encrypt(v1) ** 2...")
ctxt_powerSquare **= 2
"""Decrypt the result of Square Power of the encrypted vector."""
v_powerSquare_decrypt = HE.decrypt(ctxt_powerSquare)
"""v_powerSquare_decrypt is a list of list ie [[a, b, c,...]], so we want to flatten it to obtain [a, b, c,...]."""
v_powerSquare_decrypt_flatten = list(itertools.chain.from_iterable(v_powerSquare_decrypt))
print("Decrypt(Encrypt(v1) ** 2) -> ", v_powerSquare_decrypt_flatten)
"""Perform the Square Power on the unencrypted vectors."""
v1Power2 = [a*b for a,b in izip(v1, v1)]
print("v1 ** 2 ->", v1Power2)
"""If Decrypt(Encrypt(v1) ** 2) equal to v1 ** 2, The homeomorphic operation works and so it is a success. Else, it is a fail."""
if v_powerSquare_decrypt_flatten == v1Power2:
   print("Homeomorphic operation Square Power with operator **=2 is a success: Decrypt(Encrypt(v1) ** 2) equal to v1 ** 2.")
   number_success += 1
else:
   print("Homeomorphic operation Square Power with operator **=2 is a fail: Decrypt(Encrypt(v1) ** 2) not equal to v1 ** 2.")
   number_fail += 1


"""Skip a line."""
print("\n")


"""Perform homeomorphic Cube Power with the operator **=3 ."""
print("***Test of the homeomorphic Cube Power **=3 ***")
print("Encrypted v1: Encrypt(", v1, ")")
"""ctxt_powerCube contains Encrypt(v1). So we perform: Encrypt(v1) ** 3"""
print("Performing Encrypt(v1) ** 3...")
ctxt_powerCube **= 3
"""Decrypt the result of Cube Power of the encrypted vector."""
v_powerCube_decrypt = HE.decrypt(ctxt_powerCube)
"""v_powerCube_decrypt is a list of list ie [[a, b, c,...]], so we want to flatten it to obtain [a, b, c,...]."""
v_powerCube_decrypt_flatten = list(itertools.chain.from_iterable(v_powerCube_decrypt))
print("Decrypt(Encrypt(v1) ** 3) -> ", v_powerCube_decrypt_flatten)
"""Perform the Cube Power on the unencrypted vectors."""
v1Power3 = [a*b*c for a,b,c in izip(v1, v1, v1)]
print("v1 ** 3 ->", v1Power3)
"""If Decrypt(Encrypt(v1) ** 3) equal to v1 ** 3, The homeomorphic operation works and so it is a success. Else, it is a fail."""
if v_powerCube_decrypt_flatten == v1Power3:
   print("Homeomorphic operation Cube Power with operator **=3 is a success: Decrypt(Encrypt(v1) ** 3) equal to v1 ** 3.")
   number_success += 1
else:
   print("Homeomorphic operation Cube Power with operator **=3 is a fail: Decrypt(Encrypt(v1) ** 3) not equal to v1 ** 3.")
   number_fail += 1


"""Skip a line."""
print("\n")

"""Perform homeomorphic addition with operator + ."""
print("*** Test of the homeomorphic addition with operator + ***")
print("Encrypted v1: Encrypt(", v1, ")")
print("Encrypted v2: Encrypt(", v2, ")")
print("Performing Encrypt(v1) + Encrypt(v2)...")
ctxtAdd1_2 = ctxt12 + ctxt22 #This operation modify the ctxt1! It is a bug that should be corrected!
"""Decrypt the result of the addition of the two encrypted vectors."""
v_add_v12_v22_decrypt = HE.decrypt(ctxtAdd1_2)
"""v_add_v12_v22_decrypt is a list of list ie [[a, b, c,...]], so we want to flatten it to obtain [a, b, c,...]."""
v_add_v12_v22_decrypt_flatten = list(itertools.chain.from_iterable(v_add_v12_v22_decrypt))
"""The user can then verify if the result of the addition of the two encrypted vectors is the same that the addition of the two vectors without encryption."""
print("Decrypt(Encrypt(v1) + Encrypt(v2)) -> ", v_add_v12_v22_decrypt_flatten)
"""Perform the sum on the unencrypted vectors."""
v1Plusv2 = map(sum, izip(v1,v2))
print("v3 = v1 + v2 ->", v1Plusv2)
"""If Decrypt(Encrypt(v1) + Encrypt(v2)) equal to v1 + v2, The homeomorphic operation works and so it is a success. Else, it is a fail."""
if v_add_v12_v22_decrypt_flatten == v1Plusv2:
   """On a success, print the success and increase the number of successful tests."""
   print("Homeomorphic operation add with operator + is a success: Decrypt(Encrypt(v1) + Encrypt(v2)) equal to v1 + v2.")
   number_success += 1
else:
   """On a fail, print the fail and increase the number of fail tests."""
   print("Homeomorphic operation add with operator + is a fail: Decrypt(Encrypt(v1) + Encrypt(v2)) not equal to v1 + v2.")
   number_fail += 1


"""Skip a line."""
print("\n")


"""Perform homeomorphic Square Power with the operator **2 ."""
print("***Test of the homeomorphic Square Power **2 ***")
print("Encrypted v1: Encrypt(", v1, ")")
"""ctxt_powerSquare2 contains Encrypt(v1). So we perform: Encrypt(v1) ** 2"""
print("Performing Encrypt(v1) ** 2...")
ctxt_powerSquare2_result = ctxt_powerSquare2 ** 2
"""Decrypt the result of Square Power of the encrypted vector."""
v_powerSquare2_decrypt_result = HE.decrypt(ctxt_powerSquare2_result)
"""v_powerSquare2_decrypt_result is a list of list ie [[a, b, c,...]], so we want to flatten it to obtain [a, b, c,...]."""
v_powerSquare2_decrypt_result_flatten = list(itertools.chain.from_iterable(v_powerSquare2_decrypt_result))
print("Decrypt(Encrypt(v1) ** 2) -> ", v_powerSquare2_decrypt_result_flatten)
"""Perform the Square Power on the unencrypted vectors."""
v1Power22 = [a*b for a,b in izip(v1, v1)]
print("v1 ** 2 ->", v1Power22)
"""If Decrypt(Encrypt(v1) ** 2) equal to v1 ** 2, The homeomorphic operation works and so it is a success. Else, it is a fail."""
if v_powerSquare2_decrypt_result_flatten == v1Power22:
   print("Homeomorphic operation Square Power with operator **2 is a success: Decrypt(Encrypt(v1) ** 2) equal to v1 ** 2.")
   number_success += 1
else:
   print("Homeomorphic operation Square Power with operator **2 is a fail: Decrypt(Encrypt(v1) ** 2) not equal to v1 ** 2.")
   number_fail += 1


"""Skip a line."""
print("\n")


"""Perform homeomorphic Cube Power with the operator **3 ."""
print("***Test of the homeomorphic Cube Power **3 ***")
print("Encrypted v1: Encrypt(", v1, ")")
"""ctxt_powerCube2 contains Encrypt(v1). So we perform: Encrypt(v1) ** 3"""
print("Performing Encrypt(v1) ** 3...")
ctxt_powerCube2_result = ctxt_powerCube2 ** 3
"""Decrypt the result of Cube Power of the encrypted vector."""
v_powerCube2_decrypt_result = HE.decrypt(ctxt_powerCube2_result)
"""v_powerCube2_decrypt_result is a list of list ie [[a, b, c,...]], so we want to flatten it to obtain [a, b, c,...]."""
v_powerCube2_decrypt_result_flatten = list(itertools.chain.from_iterable(v_powerCube2_decrypt_result))
print("Decrypt(Encrypt(v1) ** 3) -> ", v_powerCube2_decrypt_result_flatten)
"""Perform the Cube Power on the unencrypted vectors."""
v1Power32 = [a*b*c for a,b,c in izip(v1, v1, v1)]
print("v1 ** 3 ->", v1Power32)
"""If Decrypt(Encrypt(v1) ** 3) equal to v1 ** 3, The homeomorphic operation works and so it is a success. Else, it is a fail."""
if v_powerCube2_decrypt_result_flatten == v1Power3:
   print("Homeomorphic operation Cube Power with operator **3 is a success: Decrypt(Encrypt(v1) ** 3) equal to v1 ** 3.")
   number_success += 1
else:
   print("Homeomorphic operation Cube Power with operator **3 is a fail: Decrypt(Encrypt(v1) ** 3) not equal to v1 ** 3.")
   number_fail += 1

"""Skip a line."""
print("\n")
print("Number of successful tests: ", number_success)
print("Number of fail tests: ", number_fail)
print("\n")


"""If the user has specify the -g option, we display a graph of the succesful tests versus the fail tests."""
if args.graph:
   # Pie chart, where the slices will be ordered and plotted counter-clockwise:
   labels = 'Success', 'Fails'
   sizes = [number_success, number_fail]
   explode = (0.1, 0)  # only "explode" the 1er slice (i.e. 'Success')

   fig1, ax1 = plt.subplots()
   ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
   ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
   plt.title("Succesful tests versus fail tests.")

   plt.show()




"""print("------------------TEST Polynomial function----------------------")

a0 = [3,3,3,3,3]
a1 = [5,5,5,5,5]
a2 = [2,2,2,2,2]
a3 = [4,4,4,4,4]

pltxt1 = PyPtxt(a0, HE)
pltxt2 = PyPtxt(a1, HE)
pltxt3 = PyPtxt(a2, HE)
pltxt4 = PyPtxt(a3, HE)

cytxt1 = HE.encrypt(pltxt1)
cytxt2 = HE.encrypt(pltxt2)
cytxt3 = HE.encrypt(pltxt3)
cytxt4 = HE.encrypt(pltxt4)

coeff = [cytxt1, cytxt2, cytxt3, cytxt4]

ctxt1polynomial = ctxt1.polynomialMult(ctxt1, coeff)
result = HE.decrypt(ctxt1polynomial)
print("Polynomial result: ", result)"""
