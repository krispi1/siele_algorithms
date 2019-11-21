""" 

# For more algorithms here's the link:
# https://github.com/krispi1/siele_algorithms

This repo is a work-in-progress. I will keep posting to it.

I intend to give you concise and accurate information on a 
number of algorithms to help you understand them really fast.

I am also learning in the process of publishing them. So if 
you find any mistake or inaccuracy please be kind, 
fork the repo, clone it, make an edit and make a pull request.

If you have a suggestion, email me on sielekrisp@gmail.com

"""

##--------------------------------------------------------

# Below you'll find one implementation of Bubble Sort

# bubble_sort

##--------------------------------------------------------

""" 
##----------------------Bubble Sort----------------------

Bubble Sort compares adjacent array elements in pairs starting 
with the first two; let's call them left and right. It swaps 
them only if the left item is greater than the right item.

It loops through the entire array or list repeatedly until
all items are sorted.

Bubble Sort is also known as: 
  -- sinking sort

##--------------------------------------------------------

# Bubble Sort Algorithm Analysis

Bubble Sort is a VERY SLOW sorting algorithm.

Suppose we have n items to sort:

Time complexity:
Worst-case:       O(n^2) comparisons
                  O(n^2) swaps
Best-case:        O(n)   comparisons --> if array is sorted already
                  O(1)   swaps --> if input array has two items
Average-case:     O(n^2) comparisons
                  O(n^2) swaps

Space complexity:
Worst-case:       O(1)   auxiliary

##--------------------------------------------------------

# References:
# https://en.wikipedia.org/wiki/Bubble_sort
# https://brilliant.org/wiki/bubble-sort/#
# https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm

"""

##--------------------------------------------------------

##---------I use these lines to visually separate--------- 
##--------code blocks and guide you on which block--------
##--------to comment / uncomment and run as a unit--------

##--------------------------------------------------------

# Bubble Sort with comments and simulation
# Please run this code and scrutinize the result

# One thing you'll notice from the results is that the largest
# element bubbles all the way to the end (extreme right).

# The process is repeated in each iteration until the entire
# list is fully sorted.

##------------------------Challenge------------------------
# You may also tweak the code so the algorithm has the 
# smallest element bubble all the way to the front (left).

##--------------------------------------------------------
# Bubble Sort with simulation

def bubble_sort(rawList, simulation=True):
  print("Input  array: ", rawList)
  print("Array length: ", len(rawList))
  print()
  
  swapped = True
  iteration = 0
  print("Iteration\t Starting Index\t Swaps \t\t Array State")
  print()
  
  while swapped:
    swapped = False
    for i in range(0, len(rawList) - 1):
      if rawList[i] > rawList[i + 1]:
        # If left item is greater than the right one, swap them
        rawList[i], rawList[i + 1] = rawList[i + 1], rawList[i]
        swapped = True

        if simulation:
          iteration = iteration + 1
          print(iteration, "\t\t", i, "\t\t", 
          '%d and %d  ' %(rawList[i + 1], rawList[i]) if 
          swapped else 'Nothing Swapped!', "\t", rawList)

  print()
  print("Sorted array: ", rawList)
  return rawList

##--------------------------------------------------------

""" 
# Bubble Sort without comments

def bubble_sort(rawList):
  swapped = True  

  while swapped:
    swapped = False
    
    for i in range(0, len(rawList) - 1):
      if rawList[i] > rawList[i + 1]:
        rawList[i], rawList[i + 1] = rawList[i + 1], rawList[i]
        swapped = True

  print(rawList)
  return rawList 
"""

##--------------------------------------------------------

# This is a helper function to run bubble_sort

def run_bubble_sort(func, inputList):
  print()
  print('Result from', func.__name__)
  func(inputList)
  print('--------------------------------------------------------')
  print()

##--------------------------------------------------------

if __name__ == "__main__":
  # Try bubble_sort
  
  # Number of iterations performed varies with item values
  myList = ([82, 16, 99, 40, 12, 91, 2, 9, 4, 7])
  run_bubble_sort(bubble_sort, myList)

  myList = ([82, 16])
  run_bubble_sort(bubble_sort, myList)

  myList = ([96, 12, 82])
  run_bubble_sort(bubble_sort, myList)

  # What happens when the input is sorted
  myList = ([12, 19, 30])
  run_bubble_sort(bubble_sort, myList)

  # Observe the number of iterations performed on a sorted list
  myList = ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
  run_bubble_sort(bubble_sort, myList)

##--------------------------------------------------------
