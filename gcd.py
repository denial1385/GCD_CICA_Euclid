
##__author__ = 'n91bu1n15'
#To get the greatest common divisor, 1 way is to use the consecutive integer check (CIC) method.
#This method divides both 2 random numbers, m and n by an integer,
# and sees if the remainder is 0 for both of them.
#If it is, it returns that integer as the answer.
#If it's not, it decrements the integer by 1, & tries again.
#Since the GCD can't be larger than the smallest of the two divisors (m and n).                                                                                                                                                                                                                                           'this algorithm starts the division process using the smallest divisor, and counting down from there.

import random

def main():

 #CIC algorithm global variables:
 iterationsArray = []
 randomNumbersArray1 = []
 randomNumbersArray2 = []
 commonDivisorArray = []

 #euclids algorithm global variables:
 euclidsrandomNumbersArray1 = []
 euclidsrandomNumbersArray2 = []

 maxIterations = 0
 minIterations = 0
 iterationSum = 0

 for x in range (0,100):
    print ("\nInstance Number: ", x)

    #variable declaration
    instanceCounter = 101           #counts down from 100 to 1
    iterationCounter = 0            #keeps track of iteration per int pair in question

    #iterationsArray = [1,2]

    gotchaFlag = False              #boolean flag, checks if this is common divisor


    random.seed()
    someRandF = random.randint(1000, 20000)
    #someRandF = 462
    random.seed()
    someRandG = random.randint(1000, 20000)
    #someRandG = 1071

    print ("Random Number 1 : ", someRandF)
    print ("Random Number 2 : ", someRandG)

    if someRandF < someRandG:
        smallerFactor = someRandF
    elif someRandF == someRandG:
        print ("The random numbers are the same! /n -- Try again!")
    else:
        smallerFactor = someRandG

    print ("Smaller Factor: ", smallerFactor)

    mod1 = someRandF%smallerFactor
    mod2 = someRandG%smallerFactor

    #print ("Modulo of 1st number: ", mod1)
    #print ("Modulo of 2nd number: ", mod2)

    if mod1 == 0 and mod2 == 0:
        gotchaFlag = True
    else:
        potentialDivisor = smallerFactor

    while gotchaFlag is not True:

        potentialDivisor = potentialDivisor - 1
        iterationCounter = iterationCounter + 1

        #modulo division
        mod1 = someRandF%potentialDivisor
        mod2 = someRandG%potentialDivisor

        #if modulo is 0, then this is a divisor.
        #It would be smart to check if this is a matching divisor on the other number from the pair.
        #Otherwise, decrement int by 1, and increment counter by 1.

        if mod1 == 0 and mod2 == 0:
            print ("Number of iterations: ", iterationCounter)
            gotchaFlag = True

    print ("The GCD for ",someRandF, " and ",someRandG, " is ", potentialDivisor)
    #print ("Total iterations are ", )
        #print ("Exiting Common Divisor Array : ", commonDivisorArray)

    iterationsArray.append(iterationCounter)
    #print (iterationsArray)

    randomNumbersArray1.append(someRandF)
    randomNumbersArray2.append(someRandG)

    rNA1Length = len(randomNumbersArray1)
    rNA2Length = len(randomNumbersArray2)

    print ("rNA1Length: ", rNA1Length)
    print ("rNA1Length: ", rNA1Length)

    #euclidsrandomNumbersArray1 = randomNumbersArray1
    #euclidsrandomNumbersArray2 = randomNumbersArray2

    commonDivisorArray.append(potentialDivisor)

    maxIterations = max(iterationsArray,key=int)
    print ("Largest iteration was : ",maxIterations)

    minIterations = min(iterationsArray,key=int)
    print ("Smallest iteration was : ",minIterations)

    iterationSum = sum(iterationsArray)
    print ("Total number of iterations : ", iterationSum)

    #print ("Average of iterations : ", iterationSum/100)

    euclidsrandomNumbersArray1 = randomNumbersArray1
    euclidsrandomNumbersArray2 = randomNumbersArray2

 print ("Iterations: ", iterationsArray)
 print ("Random Number 1: ", randomNumbersArray1)
 print ("Random Number 2: ", randomNumbersArray2)

 positionOfMaxIter = iterationsArray.index(max(iterationsArray,key=int))
 print ("\n Position in Max Iterations Array: ", positionOfMaxIter)

 positionOfMinIter = iterationsArray.index(min(iterationsArray,key=int))
 print ("\n Position in Min Iterations Array: ", positionOfMinIter)

 maxNumberInRandArr1 = randomNumbersArray1.pop(positionOfMaxIter)
 maxNumberInRandArr2 = randomNumbersArray2.pop(positionOfMaxIter)
 maxGCDInCommDivArray = commonDivisorArray.pop(positionOfMaxIter)

 minNumberInRandArr1 = randomNumbersArray1.pop(positionOfMinIter)
 minNumberInRandArr2 = randomNumbersArray2.pop(positionOfMinIter)
 minGCDInCommDivArray = commonDivisorArray.pop(positionOfMinIter)

 print ("Max iterations Rand Number 1: ", maxNumberInRandArr1)
 print ("Max iterations Rand Number 2: ", maxNumberInRandArr2)
 print ("Max iterations GCD: ", maxGCDInCommDivArray)

 print ("Min iterations Rand Number 1: ", minNumberInRandArr1)
 print ("Min iterations Rand Number 2: ", minNumberInRandArr2)
 print ("Min iterations GCD: ", minGCDInCommDivArray)

 print ("\n\nThe most number of iterations used is", maxIterations, ": for GCD of (",maxNumberInRandArr1,",",
        maxNumberInRandArr2,"), which is = ",maxGCDInCommDivArray,".")
 print ("The least number of iterations used is", minIterations, ": for GCD of (",minNumberInRandArr1,",",
        minNumberInRandArr2,"), which is=",minGCDInCommDivArray,".")
 #print ("Total number of iterations :  ", iterationSum)
 print ("The average number of iterations used for all 100 pairs is ", iterationSum/100, "iterations.")


 #*************************************************
 #
 #              EUCLID'S ALGORITHM
 #
 # Subtract a smaller co-prime from a larger co-prime, and repeat the process until the difference is 0.
 #
 #*************************************************

 temp = 0
 gotEuclidsGCD = False
 euclidsGCD = 0
 euclidsCounter = 0
 euclidsCounterArray = []
 euclidsCommonDivisorArray = []
 euclidsRandomNumbersArray1 = []
 euclidsRandomNumbersArray2 = []

 #a = 1071
 #b = 462
 #GCD of test = 21

 print ("\n ***********************************************\n ****** Now Implementing: Euclid's Algorithm.... \n\n")
 print (euclidsrandomNumbersArray1)
 print (euclidsrandomNumbersArray2, "\n")

 #print ("rNA1Length: ", rNA1Length)
 #print ("rNA1Length: ", rNA1Length)

 euclidsRNA1Length = len(euclidsrandomNumbersArray1)
 euclidsRNA2Length = len(euclidsrandomNumbersArray2)

 print ("euclidsRNA1Length: ", euclidsRNA1Length)
 print ("euclidsRNA2Length: ", euclidsRNA2Length)

 if euclidsRNA1Length == euclidsRNA2Length:
     euclidsRange = euclidsRNA2Length


 while len(euclidsrandomNumbersArray1) != 0:

     euclidsCounter = 0

     print ("\nInstance Number: ", len(euclidsrandomNumbersArray1))

     #compare coprimes, make larger a and smaller b

     euclidsCandidate1 = randomNumbersArray1.pop(0)
     euclidsCandidate2 = randomNumbersArray2.pop(0)

     print ("\neuclidsCandidate1: ", euclidsCandidate1)
     print ("euclidsCandidate2: ", euclidsCandidate2)

     if euclidsCandidate1 > euclidsCandidate2:
         a = euclidsCandidate1
         b = euclidsCandidate2
     else:
         a = euclidsCandidate2
         b = euclidsCandidate1

     temp = a - b

     print ( "First go: a - b =", temp)

     while b != temp:

         euclidsCounter += 1

         #print ("\nHi!\n")

         if temp > b:
            temp = temp - b
            #print ("Temp1: ", temp)
            #print ("B1:",b,"/n")

         elif temp < b:
                newA = b
                b = temp
                temp = newA - b

                #print ("newA2: ",newA)
                #print ("Temp2: ",temp)
                #print ("b2: ",b,"\n")

         else:
                euclidsGCD = b
                print ("True -> euclidsGCD:", euclidsGCD, " b:", b)
                gotEuclidsGCD = True



     euclidsGCD = b
     print ("True -> euclidsGCD:", euclidsGCD, " b:", b)

     print ("Iterations for this instance: ", euclidsCounter)


     #***********************************************



 #print ("The GCD for ",euclidsCandidate1, " and ",euclidsCandidate2, " is ", euclidsGCD)
    #print ("Total iterations are ", )
        #print ("Exiting Common Divisor Array : ", commonDivisorArray)

     euclidsCounterArray.append(euclidsCounter)
     euclidsRandomNumbersArray1.append(euclidsCandidate1)
     euclidsRandomNumbersArray2.append(euclidsCandidate2)

     euclidsCommonDivisorArray.append(euclidsGCD)


 print ("\n\nEuclids Counter Array: ", euclidsCounterArray)

 print ("EuclidsRandomNumbersArray1: ", euclidsRandomNumbersArray1)
 print ("EuclidsRandomNumbersArray2: ", euclidsRandomNumbersArray2)

    #rNA1Length = len(randomNumbersArray1)
    #rNA2Length = len(randomNumbersArray2)

    #print ("rNA1Length: ", rNA1Length)
    #print ("rNA1Length: ", rNA1Length)

    #euclidsrandomNumbersArray1 = randomNumbersArray1
    #euclidsrandomNumbersArray2 = randomNumbersArray2

 print ("\n\nCICA's GCD Array: ", commonDivisorArray)
 print ("\nEuclid's GCD Array: ", euclidsCommonDivisorArray)


 #******************************************************************************


 euclidsPositionOfMaxIter = euclidsCounterArray.index(max(euclidsCounterArray,key=int))
 print ("\n Position in Max Iterations Array: ", euclidsPositionOfMaxIter)

 euclidsPositionOfMinIter = euclidsCounterArray.index(min(euclidsCounterArray,key=int))
 print ("\n Position in Min Iterations Array: ", euclidsPositionOfMinIter)

 euclidsMaxNumberInRandArr1 = euclidsRandomNumbersArray1.pop(euclidsPositionOfMaxIter)
 euclidsMaxNumberInRandArr2 = euclidsRandomNumbersArray2.pop(euclidsPositionOfMaxIter)
 euclidsMaxGCDInCommDivArray = euclidsCommonDivisorArray.pop(euclidsPositionOfMaxIter)

 euclidsMinNumberInRandArr1 = euclidsRandomNumbersArray1.pop(euclidsPositionOfMinIter)
 euclidsMinNumberInRandArr2 = euclidsRandomNumbersArray2.pop(euclidsPositionOfMinIter)
 euclidsMinGCDInCommDivArray = euclidsCommonDivisorArray.pop(euclidsPositionOfMinIter)

 print ("Max iterations Rand Number 1: ", euclidsMaxNumberInRandArr1)
 print ("Max iterations Rand Number 2: ", euclidsMaxNumberInRandArr2)
 print ("Max iterations GCD: ", euclidsMaxGCDInCommDivArray)

 print ("Min iterations Rand Number 1: ", euclidsMinNumberInRandArr1)
 print ("Min iterations Rand Number 2: ", euclidsMinNumberInRandArr2)
 print ("Min iterations GCD: ", euclidsMinGCDInCommDivArray)









 #   ******* PROOF ********

 # CICA's Algorithm Results:

 print ("\n>>>> \n (1) CICA'S ALGORITHM:")

 print ("\n\nThe most number of iterations used is", maxIterations, ": for GCD of (",maxNumberInRandArr1,",",
        maxNumberInRandArr2,"), which is = ",maxGCDInCommDivArray,".")
 print ("The least number of iterations used is", minIterations, ": for GCD of (",minNumberInRandArr1,",",
        minNumberInRandArr2,"), which is =",minGCDInCommDivArray,".")
 #print ("Total number of iterations :  ", iterationSum)
 print ("The average number of iterations used for all 100 pairs is ", iterationSum/100, "iterations.")

 # Euclid's Algorithm Results:

 print ("\n>>>> \n (2) EUCLID'S ALGORITHM:")

 euclidsMaxIterations = max(euclidsCounterArray,key=int)
 print ("The most number of iterations used is", euclidsMaxIterations, ": for GCD of (",euclidsMaxNumberInRandArr1,",",
        euclidsMaxNumberInRandArr2,"), which is =",euclidsMaxGCDInCommDivArray,".")

 euclidsMinIterations = min(euclidsCounterArray,key=int)
 print ("The least number of iterations used is", euclidsMinIterations, ": for GCD of (",euclidsMinNumberInRandArr1,",",
        euclidsMinNumberInRandArr2,"), which is =",euclidsMinGCDInCommDivArray,".")

 euclidsIterationSum = sum(euclidsCounterArray)
 print ("Total number of iterations : ", euclidsIterationSum)

 print ("The average number of iterations used for all 100 pairs is ",  int (euclidsIterationSum/100), "iterations.")


#***********

                #**********

                                #*************
if __name__ == '__main__':
        main()








