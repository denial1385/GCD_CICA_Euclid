GCD_CICA_Euclid
===============

Task: Implement a program, using a language of your choice, to calculate the Greatest Common Divisor,
of 2 random coprimes in the range of 1000 - 20,000. Use a counter to record number of integers checked, 
before the GCD is found for each pair. 

  (1) Use the Consecutive Integer Checking Algorithm, and calculate the most iterations, the least iterations,
      and the average iterations for each pair:
      
      The program checks if the modulo of dividing the larger dividend by the smaller divisor is 0, 
      for each pair, by an ever-decreasing int variable. This int variable (labelled "smallerFactor")
      starts from the lesser of the paired numbers, since this is the largest number 
      that can feasibly be a divisor. If the mod is 0 for BOTH, this is the greatest divisor of both. 
      Otherwise, step down an int and try that again. 
      
      - The program seeds and populates an array using Python's random() class, and sets the bounds to match 
      1000 - 20,000. From this result, it then evaluates which of the 2 is smaller and sets that as the 
      initialization point of mod division. It performs one set of mod divison and checks for equality to 0.
      A boolean flag (gotchaFlag) marks attainment of the GCD, otherwise, while gotchaFlag is False, 
      it decrements the potential divisor counter to skip to the next lower int, and increments the iteration 
      counter that checks how many steps or iterations this algorithm takes to arrive at the GCD.
      
      - The program then appends the discovered GCD into a list, appends each random number from the pair 
      into either matching array ( i.e. randomNumber(x) is placed in randomNumberArray(x), where x is either
      1 or 2. It finds the length of the 2 latter list i.e. randomNumberArray1 or randomNumberArray2, since it will
      be used as a counter in part (2) below. 
      
      -The calculation of most, least and average number of iterations is performed by a simple list.index(max),
      a list.index(min), and a sum(list) / 100, respectively. 
      
  (2) Implement Euclid's algorithm, using the same random numbers in (1) above, and compare similar outputs:
  
      The program uses the pairs generated in (1) above, which were stored in 2 arrays, randomNumberArray1 and 
      randomNumberArray2, and first compares each number to find the smaller of the pair. It subtracts the smaller
      subtrahend from the larger minuend, and this is considered one iteration, or one operation on the ints. 





      N/B: The Python version is 3.3 - 64 bit.
      
      

