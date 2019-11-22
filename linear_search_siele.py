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

# Below you'll find one implementation of Linear Search

# linear_search

##--------------------------------------------------------

""" 
##---------------------Linear Search---------------------

Linear Search takes an array/list and a target item.

Linear Search starts at index 0 (the first element) and goes
sequentially until it either finds the target item and returns
its index, or it terminates with a return of -1 or None in case 
it reaches the end of the list without finding it.

Linear Search pros:
It is simple to implement.
It is only suitable for small lists e.g. of 100 items or less.

Linear Search cons:
Linear Search is rarely practical because it is fairly slow.

For larger lists, other algorithms e.g. binary search are preferred.

Linear Search is also known as: 
  -- sequential search

##--------------------------------------------------------

# Linear Search Algorithm Analysis

Linear Search is not a fast search algorithm.

Suppose we have n items to search through:

Time complexity:
Worst-case:       O(n)
Best-case:        O(1)
Average-case:     O(n)

Space complexity:
Worst-case:       O(1) iterative

##--------------------------------------------------------

# References:
# https://en.wikipedia.org/wiki/Linear_search

"""

##--------------------------------------------------------

##---------I use these lines to visually separate--------- 
##--------code blocks and guide you on which block--------
##--------to comment / uncomment and run as a unit--------

##--------------------------------------------------------
# linear_search with comments

def linear_search(inputList, targetValue):
  print()
  print("Result  from:", linear_search.__name__)
  print("Input  array:", inputList)

  for i in range(len(inputList)):
    # print(i, inputList[i])
    if inputList[i] == targetValue:
      print()
      print('%d found at index %d' %(targetValue, i))
      return i

  print()
  print('%d not found in list!' %targetValue)
  return None

##--------------------------------------------------------
""" 
# linear_search without comments

def linear_search(inputList, targetValue):
  print()

  for i in range(len(inputList)):
    if inputList[i] == targetValue:
      return i

  return None
"""
##--------------------------------------------------------

# This is a helper function to run linear_search

def run_linear_search(func, inputList, findList):
  for item in findList:
    func(inputList, item)
    print('--------------------------------------------------------')
  
##--------------------------------------------------------

if __name__ == "__main__":
  itemsToFind = [5, 7, 9, 12]
  myList = [34, 12, 54, 6, 2, 9, 10, 4, 7, 3]

  run_linear_search(linear_search, myList, itemsToFind)

##--------------------------------------------------------

