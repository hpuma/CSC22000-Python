from algorithm_implementations import InsertionSort,MergeSort,HeapSort,QuickSort,QuickSortPivot
from random import randrange
import timeit
import time
import sys
# ALGORITHM TEST TOOLS
# Returns a boolean whether or not the input array is sorted in non decreasing order
# Starts from the second index and compares it to the index before 
def isSorted(A):
    if(len(A) <= 1):
        return True
    for i in range(1,len(A)): 
        if(A[i-1] > A[i]): # If the previous value is greater than the current value, then the array is not sorted!
            return False
    return True # All previous values have been less than the current iterated value
# Takes in the runtime of the algorithm and prints it in the appropriate matter depending on the time length
def print_runtime(t):
    if(t < 1.0): 
        print("Time:\t",round(t*1000.0,12),"milliseconds")
    elif(t >= 1.0 and t < 60.0):
        print("Time:\t",round(t,6),"seconds") 
    elif(t >= 60.0 and t < 3600.0):
        print("Time:\t",round(t/60.0,6),"minutes") 
    elif(t >= 3600.0):
        print("Time:\t",round(t/3600.0,6),"hours") 
# Prints the lists details depending on its size and current context
def print_list(A, before):
    if(before == True):
        print("Before:\t",end="")
    else:
        print("After:\t",end="")
    if len(A) <= 100:
        print(A)
    print("Sorted:\t",isSorted(A)) 
# Creates a random_list of size "list_size" where the range of list values is from 1 to list_size-1
def BuildList(list_size):
    input_values = dict() # Creating an empty dictionary to generate distinct random values
    last_val = list_size + 1 # Last possible range for the randomly generated array
    while (len(input_values) < list_size): # Generating a random int value for each index in the empty list
        rand_key = False # Set a generated random key to false
        while(not rand_key):# Keep generating a random value until we find a value that is not in the dictionary meaning it's unique
            rand_val = randrange(1,last_val)
            if input_values.get(rand_val) == None:# When we have generated a unique int 
                input_values[rand_val] = True
                rand_key = True
    return list(input_values.keys())
# Wraps a function with arguments and returns the same function as a function with no arguments
# This is used along side timeit.timeit
def fwrap(func,*args,**kwargs):
        def fwrapper():
            return func(*args,**kwargs)
        return fwrapper
# Tests a single algorithm function and Printing its results
def algorithm_test(algorithm,test_list,p=0,r=0):
    # Wraps the algorithm depending if it has additional arguments like "MergeSort" , and "Quick Sort"
    if(p == 0 and r!=0):
        wrapped_algorithm = fwrap(algorithm,test_list,p,r)
    else: 
        wrapped_algorithm = fwrap(algorithm,test_list)
    print("Testing:\t", algorithm.__name__) # Prints the current algorithm that is being tested
    start_time = time.time() # Alternative measuring tool for algorithm
    print_runtime(timeit.timeit(wrapped_algorithm,number=1)) # Tests the algorithms sorting
    print("Alt ",end="") # Prints the alternate method for measuring the algorithm time
    print_runtime(time.time()-start_time) # 
    # Prints the output of the test array after the algorithm iff the array is less than a 100
    # Also prints whether or not the array has been successfully sorted
    if(len(test_list) >=2 and len(test_list) <=100): 
        print("Output:",test_list,"\nSorted:\t",isSorted(test_list))
    elif(len(test_list) > 100):
        print("Sorted:\t",isSorted(test_list))
    print("")
# Tests all the algorithms, Big funtion that applies algorithm_test to all algorithms
def test_all_algorithms(list_size):
    print("Generating Random List:\tn =",list_size)
    random_list = BuildList(list_size) # Generating the "list_size" size random list 
    last_index = list_size-1 # Last index for merge sort and quick sort algorithms
    # Print the test list if it's less than size 100
    # Also assure that the test array is unsorted
    if len(random_list) > 0 and len(random_list) <= 100:
        print("Test List:\t",random_list)
    elif len(random_list) > 100 and len(random_list) > 0:
        print("Non-Empty List Length =",len(random_list),"\nSorted:\t",isSorted(random_list))
    print("")
    # Testing all algorithms
    # NOTE: Made sure that random array copies were passed into the algorithm functions
    algorithm_test(InsertionSort,list.copy(random_list))
    algorithm_test(MergeSort,list.copy(random_list),0,last_index)
    algorithm_test(HeapSort,list.copy(random_list))
    algorithm_test(QuickSort,list.copy(random_list),0,last_index)
    algorithm_test(QuickSortPivot,list.copy(random_list),0,last_index)