
##__author__ = 'n91bu1n15'
#To get the greatest common divisor, 1 way is to use the consecutive integer check (CIC) method.
#This method divides both 2 random numbers, m and n by an integer,
# and sees if the remainder is 0 for both of them.
#If it is, it returns that integer as the answer.
#If it's not, it decrements the integer by 1, & tries again.
#Since the GCD can't be larger than the smallest of the two divisors (m and n).                                                                                                                                                                                                                                           'this algorithm starts the division process using the smallest divisor, and counting down from there.

import random

def main():

 #CIC algorithm variables:
 iterationsArray = []           #keeps track of how many iterations an algm takes to get GCD
 randomNumbersArray1 = []       #keeps track of a random number in pair
 randomNumbersArray2 = []       #keeps track of other random number in pair
 commonDivisorArray = []        #keeps track of pair's GCD

 maxIterations = 0              #largest int in iterationsArray
 minIterations = 0              #smallest int in iterationsArray
 iterationSum = 0               #sums all ints in iterationsArray

 #euclids algorithm variables:
 euclidsrandomNumbersArray1 = []    #copies randomNumbersArray1 to Euclid's Algorithm
 euclidsrandomNumbersArray2 = []    #copies randomNumbersArray2 to Euclid's Algorithm

 print ("Program start...")


 for x in range (0,100):                #how to repeat operation for 100 pairs of ints
    #print ("\nInstance Number: ", x)

    #variable declaration
    potentialDivisor = 0
    #instanceCounter = 101          #counts down from 100 to 1
    iterationCounter = 0            #keeps track of iteration per int pair in question
    gotchaFlag = False              #boolean flag, checks and sets True if common divisor found

    random.seed()                               #seeds random number generator
    someRandF = random.randint(1000, 20000)     #gets first random int from specified range
    #someRandF = 462                            #test input
    random.seed()
    someRandG = random.randint(1000, 20000)
    #someRandG = 1071

    #print ("Random Number 1 : ", someRandF)
    #print ("Random Number 2 : ", someRandG)

    if someRandF < someRandG:                   #checks which is larger before mod division
        smallerFactor = someRandF
    elif someRandF == someRandG:
        print ("The random numbers are the same! /n -- Try again!")
        return
    else:
        smallerFactor = someRandG

    #print ("Smaller Factor: ", smallerFactor)

    #Mod Division:
    mod1 = someRandF%smallerFactor
    mod2 = someRandG%smallerFactor

    #print ("Modulo of 1st number: ", mod1)
    #print ("Modulo of 2nd number: ", mod2)

    if mod1 == 0 and mod2 == 0:             #if both mods are 0, no need to step into algorithm
        gotchaFlag = True                   #bool flag, True if previous calculation resulted in GCD
    else:
        potentialDivisor = smallerFactor    #otherwise, the potential GCD is the smaller number

    while gotchaFlag is not True:

        potentialDivisor = potentialDivisor - 1     #subtracts one from a potential, & retries
        iterationCounter = iterationCounter + 1    #records each iteration or each int attempted

        #modulo division
        mod1 = someRandF%potentialDivisor
        mod2 = someRandG%potentialDivisor

        #if modulo is 0, then this is a divisor.
        #It would be smart to check if this is a matching divisor on the other number from the pair.
        #Otherwise, decrement int by 1, and increment counter by 1.

        if mod1 == 0 and mod2 == 0:
            #print ("Number of iterations: ", iterationCounter)
            gotchaFlag = True

    iterationsArray.append(iterationCounter)


    #print ("The GCD for ",someRandF, " and ",someRandG, " is ", potentialDivisor)

    #print ("Exiting Common Divisor Array : ", commonDivisorArray)

    cicaGCD = potentialDivisor                  #this divisor is the GCD using CICA


    #print (iterationsArray)

    randomNumbersArray1.append(someRandF)       #pushes this int into an array for use in Euclid's Alg
    randomNumbersArray2.append(someRandG)
    commonDivisorArray.append(cicaGCD)

    rNA1Length = len(randomNumbersArray1)
    rNA2Length = len(randomNumbersArray2)

    #print ("rNA1Length: ", rNA1Length)
    #print ("rNA1Length: ", rNA1Length)

    #euclidsrandomNumbersArray1 = randomNumbersArray1
    #euclidsrandomNumbersArray2 = randomNumbersArray2

    #commonDivisorArray.append(potentialDivisor)

 maxIterations = max(iterationsArray,key=int)            #gets largest iteration value
    #print ("Largest iteration was : ",maxIterations)       #gets smallest iteration value

 minIterations = min(iterationsArray,key=int)            #gets smallest iteration value
    #print ("Smallest iteration was : ",minIterations)

 iterationSum = sum(iterationsArray)                     #gets sum of iteration values
    #print ("Total number of iterations : ", iterationSum)

 euclidsrandomNumbersArray1 = randomNumbersArray1        #copies arrays of random ints for Euclid's Alg
 euclidsrandomNumbersArray2 = randomNumbersArray2

 #print ("Iterations: ", iterationsArray)
 #print ("Random Number 1: ", randomNumbersArray1)
 #print ("Random Number 2: ", randomNumbersArray2)

 positionOfMaxIter = iterationsArray.index(max(iterationsArray,key=int))     #gets position in array of max rand
 #print ("\n Position in Max Iterations Array: ", positionOfMaxIter)

 positionOfMinIter = iterationsArray.index(min(iterationsArray,key=int))    #gets position in array of min rand
 #print ("\n Position in Min Iterations Array: ", positionOfMinIter)

 maxNumberInRandArr1 = randomNumbersArray1.pop(positionOfMaxIter)       #pops value at position retrieved above
 maxNumberInRandArr2 = randomNumbersArray2.pop(positionOfMaxIter)
 maxGCDInCommDivArray = commonDivisorArray.pop(positionOfMaxIter)

 minNumberInRandArr1 = randomNumbersArray1.pop(positionOfMinIter)
 minNumberInRandArr2 = randomNumbersArray2.pop(positionOfMinIter)
 minGCDInCommDivArray = commonDivisorArray.pop(positionOfMinIter)

 #print ("Max iterations Rand Number 1: ", maxNumberInRandArr1)
 #print ("Max iterations Rand Number 2: ", maxNumberInRandArr2)
 #print ("Max iterations GCD: ", maxGCDInCommDivArray)
 #
 #print ("Min iterations Rand Number 1: ", minNumberInRandArr1)
 #print ("Min iterations Rand Number 2: ", minNumberInRandArr2)
 #print ("Min iterations GCD: ", minGCDInCommDivArray)

 #print ("\n\nThe most number of iterations used is", maxIterations, ": for GCD of (",maxNumberInRandArr1,",",
 #       maxNumberInRandArr2,"), which is = ",maxGCDInCommDivArray,".")
 #print ("The least number of iterations used is", minIterations, ": for GCD of (",minNumberInRandArr1,",",
 #       minNumberInRandArr2,"), which is=",minGCDInCommDivArray,".")
 ##print ("Total number of iterations :  ", iterationSum)
 #print ("The average number of iterations used for all 100 pairs is ", iterationSum/100, "iterations.")


 # CICA's Algorithm Results:

 print ("\n>>>> \n (1) CYCLIC INT CHECKING ALGORITHM:")

 print ("\nThe most number of iterations used is", maxIterations, ": for GCD of (",maxNumberInRandArr1,",",
        maxNumberInRandArr2,"), which is = ",maxGCDInCommDivArray,".")
 print ("The least number of iterations used is", minIterations, ": for GCD of (",minNumberInRandArr1,",",
        minNumberInRandArr2,"), which is =",minGCDInCommDivArray,".")
 #print ("Total number of iterations :  ", iterationSum)
 print ("The average number of iterations used for all 100 pairs is ", iterationSum/100, "iterations.")


 #*************************************************
 #
 #              EUCLID'S ALGORITHM
 #
 # Subtract a smaller co-prime from a larger co-prime, and repeat the process until the difference is 0.
 #
 #*************************************************

 temp = 0                               #temporary variable from subtraction operations
 gotEuclidsGCD = False                  #bool flag set True once GCD is found
 euclidsGCD = 0
 euclidsCounter = 0                     #keeps track of iteration per int pair in question
 euclidsCounterArray = []               #keeps track of euclidsCounter's value
 euclidsCommonDivisorArray = []         #keeps track of pair's GCD
 euclidsRandomNumbersArray1 = []
 euclidsRandomNumbersArray2 = []

 #a = 1071                              #test data
 #b = 462
 #GCD of test = 21

 #print ("\n ******************************\n\n ****** Now Implementing: Euclid's Algorithm ... \n\n")
 #print (euclidsrandomNumbersArray1)
 #print (euclidsrandomNumbersArray2, "\n")

 #print ("rNA1Length: ", rNA1Length)
 #print ("rNA1Length: ", rNA1Length)

 euclidsRNA1Length = len(euclidsrandomNumbersArray1)    #useful for cross check & in while loop below
 euclidsRNA2Length = len(euclidsrandomNumbersArray2)

 #print ("euclidsRNA1Length: ", euclidsRNA1Length)
 #print ("euclidsRNA2Length: ", euclidsRNA2Length)

 if euclidsRNA1Length == euclidsRNA2Length:             #little check if both array lengths are equal
     euclidsRange = euclidsRNA2Length

 while len(euclidsrandomNumbersArray1) != 0:

     euclidsCounter = 0                                 #re-initializes instance counter for each loop

     #print ("\nInstance Number: ", len(euclidsrandomNumbersArray1))

     #compare coprimes, make larger a and smaller b

     euclidsCandidate1 = randomNumbersArray1.pop(0)     #gets matching pair from array from CICA
     euclidsCandidate2 = randomNumbersArray2.pop(0)

     #print ("\neuclidsCandidate1: ", euclidsCandidate1)
     #print ("euclidsCandidate2: ", euclidsCandidate2)

     if euclidsCandidate1 > euclidsCandidate2:          #check for smaller int to use as subtrahend
         a = euclidsCandidate1                          #to simplify using a - b as formula
         b = euclidsCandidate2
     else:
         a = euclidsCandidate2
         b = euclidsCandidate1

     temp = a - b

     #if result after subtraction is similar to the subtrahend, the next subtraction operation
     #would equals 0, therefore this is the GCD.

     while b != temp:

         euclidsCounter += 1                    #keeps track of iteration per int pair in question

         #print (euclidsCounter)

         if temp > b:                           #still more operations to be done, proceed as is
            temp = temp - b
            #print ("Temp1: ", temp)
            #print ("B1:",b,"/n")

         elif temp < b:                         #no operations left
                newA = b                        #makes b be the new "a", the minuend
                b = temp                        #makes the temp from before the subtrahend
                temp = newA - b                 #equivalent of a - b

         else:
                euclidsGCD = b                  #b is the GCD and set the flag to True
                #print ("True -> euclidsGCD:", euclidsGCD, " b:", b)
                gotEuclidsGCD = True

     euclidsGCD = b
     #print ("True -> euclidsGCD:", euclidsGCD, " b:", b)
     #print ("Iterations for this instance: ", euclidsCounter)

     #***********************************************

     #print ("The GCD for ",euclidsCandidate1, " and ",euclidsCandidate2, " is ", euclidsGCD)
     #print ("Total iterations are ", )
     #print ("Exiting Common Divisor Array : ", commonDivisorArray)

     euclidsCounterArray.append(euclidsCounter)                 #same as before
     euclidsRandomNumbersArray1.append(euclidsCandidate1)
     euclidsRandomNumbersArray2.append(euclidsCandidate2)

     euclidsCommonDivisorArray.append(euclidsGCD)


 #print ("\n\nEuclids Counter Array: ", euclidsCounterArray)

 #print ("EuclidsRandomNumbersArray1: ", euclidsRandomNumbersArray1)
 #print ("EuclidsRandomNumbersArray2: ", euclidsRandomNumbersArray2)

    #rNA1Length = len(randomNumbersArray1)
    #rNA2Length = len(randomNumbersArray2)

    #print ("rNA1Length: ", rNA1Length)
    #print ("rNA1Length: ", rNA1Length)

    #euclidsrandomNumbersArray1 = randomNumbersArray1
    #euclidsrandomNumbersArray2 = randomNumbersArray2

 #print ("\n\nCICA's GCD Array: ", commonDivisorArray)
 #print ("\nEuclid's GCD Array: ", euclidsCommonDivisorArray)

 #******************************************************************************

 euclidsPositionOfMaxIter = euclidsCounterArray.index(max(euclidsCounterArray,key=int)) #same as before
 #print ("\n Position in Max Iterations Array: ", euclidsPositionOfMaxIter)

 euclidsPositionOfMinIter = euclidsCounterArray.index(min(euclidsCounterArray,key=int))
 #print ("\n Position in Min Iterations Array: ", euclidsPositionOfMinIter)

 euclidsMaxNumberInRandArr1 = euclidsRandomNumbersArray1.pop(euclidsPositionOfMaxIter)
 euclidsMaxNumberInRandArr2 = euclidsRandomNumbersArray2.pop(euclidsPositionOfMaxIter)
 euclidsMaxGCDInCommDivArray = euclidsCommonDivisorArray.pop(euclidsPositionOfMaxIter)

 euclidsMinNumberInRandArr1 = euclidsRandomNumbersArray1.pop(euclidsPositionOfMinIter)
 euclidsMinNumberInRandArr2 = euclidsRandomNumbersArray2.pop(euclidsPositionOfMinIter)
 euclidsMinGCDInCommDivArray = euclidsCommonDivisorArray.pop(euclidsPositionOfMinIter)

 #print ("Max iterations Rand Number 1: ", euclidsMaxNumberInRandArr1)
 #print ("Max iterations Rand Number 2: ", euclidsMaxNumberInRandArr2)
 #print ("Max iterations GCD: ", euclidsMaxGCDInCommDivArray)
 #
 #print ("Min iterations Rand Number 1: ", euclidsMinNumberInRandArr1)
 #print ("Min iterations Rand Number 2: ", euclidsMinNumberInRandArr2)
 #print ("Min iterations GCD: ", euclidsMinGCDInCommDivArray)

 # Euclid's Algorithm Results:

 print ("\n>>>> \n (2) EUCLID'S ALGORITHM:")

 euclidsMaxIterations = max(euclidsCounterArray,key=int)
 print ("The most number of iterations used is", euclidsMaxIterations, ": for GCD of (",euclidsMaxNumberInRandArr1,",",
        euclidsMaxNumberInRandArr2,"), which is =",euclidsMaxGCDInCommDivArray,".")

 euclidsMinIterations = min(euclidsCounterArray,key=int)
 print ("The least number of iterations used is", euclidsMinIterations, ": for GCD of (",euclidsMinNumberInRandArr1,",",
        euclidsMinNumberInRandArr2,"), which is =",euclidsMinGCDInCommDivArray,".")

 euclidsIterationSum = sum(euclidsCounterArray)
 #print ("Total number of iterations : ", euclidsIterationSum)

 print ("The average number of iterations used for all 100 pairs is ",  int (euclidsIterationSum/100), "iterations.")

 print ("\n...Program end")

#***********

                #**********

                                #*************
if __name__ == '__main__':
        main()