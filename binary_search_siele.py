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

# Below you'll find three implementations of Binary Search

# binary_search
# alt_binary_search
# binary_search_recursive

##--------------------------------------------------------

""" 
##---------------------Binary Search---------------------

Binary Search takes a SORTED LIST (array) and the target item 
(i.e. what we are searching for) then uses 
pseudo-divide-and-conquer strategy by always checking the 
value at its mid-point to see if it matches the target item we 
are looking for and then breaking up the list if it doesn't.

Imagine you have a cursor that always points at the mid-point.

At each iteration, it computes the mid-point then compares
the target item with the value at the mid-point. If the 
target item is equal to that at the mid-point, then it's a
success; so it returns the mid-point's index.

If the target item is less than that at the mid-point, it 
discards everything from the mid-point to the right.

If the target item is more than that at the mid-point, it 
discards everything from the mid-point to the left.

This process is repeated for each iteration until the cursor
has zoned-in on the mid-point when the list can no longer be 
halved.

If at this point it hasn't found a match for our target item
then it returns None or -1 to signify that the target item was 
not found in our sorted list.

Binary Search is also known as: 
  -- half-interval search
  -- logarithmic search
  -- binary chop

##--------------------------------------------------------

# Binary Search Algorithm Analysis

Binary Search is a FAST search algorithm.

Suppose we have n items to search through:

Time complexity:
Worst-case:       O(log n)
Best-case:        O(1)
Average-case:     O(log n)

Space complexity:
Worst-case:       O(1)

##--------------------------------------------------------

# References:
# https://en.wikipedia.org/wiki/Binary_search_algorithm
# https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm
# https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
# https://www.codesdope.com/course/algorithms-binary-search/

"""

##--------------------------------------------------------

##---------I use these lines to visually separate--------- 
##--------code blocks and guide you on which block--------
##--------to comment / uncomment and run as a unit--------

##--------------------------------------------------------

# binary_search with comments

def binary_search(sortedList, targetItem):
  sortedList = sorted(sortedList) # Ensure list is sorted
  print() # Print new line for readability
  print(sortedList)

  # Declare start and end indexes in one swoop
  start, end = 0, len(sortedList) - 1
  
  while start <= end:
    # Always find the new mid-point with every loop
    midIndex = int((start + end ) / 2)
    # Always find the mid value with every loop
    midValue = sortedList[midIndex]

    if midValue == targetItem:
      print('Found %d at index %d' %(targetItem, midIndex))
      return midIndex
    
    # Item to find is less than value at mid-point
    elif targetItem < midValue:
      end = midIndex - 1

    # Item to find is greater than value at mid-point
    elif targetItem > midValue:
      start = midIndex + 1

  print('Item %d not found!' %targetItem)
  return None

##--------------------------------------------------------

""" 
# binary_search without comments

def binary_search(sortedList, targetItem):
  sortedList = sorted(sortedList)
  print()

  start, end = 0, len(sortedList) - 1
  
  while start <= end:
    midIndex = int((start + end) / 2)
    midValue = sortedList[midIndex]

    if targetItem == midValue:
      return midIndex

    elif targetItem < midValue:
      end = midIndex - 1 

    elif targetItem > midValue:
      start = midIndex + 1

  return None

 """

##--------------------------------------------------------

# Try binary_search
print()
print('Results from binary_search')
# myList contains prime numbers between 1 and 100
myList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

binary_search(myList, 13)
binary_search(myList, 37)
binary_search(myList, 9)
binary_search(myList, 89)

##--------------------------------------------------------

# alt_binary_search without comments

def alt_binary_search(sortedList, targetItem):
  sortedList = sorted(sortedList) # Ensure list is sorted
  start, end = 0, len(sortedList) - 1
  print()
  
  while start != end:
    import math
    midIndex = math.ceil((start + end) / 2)   
    
    if targetItem < sortedList[midIndex]:
      end = midIndex - 1
    else: start = midIndex

  if targetItem == sortedList[start]:
    return start

  return None

##--------------------------------------------------------

# Try alt_binary_search
print()
myList = [34, 12, 54, 6, 2, 9, 10, 4, 7, 3]
print(myList)
print('Results from alt_binary_search')
print(alt_binary_search(myList, 1))
print(alt_binary_search(myList, 34))
print(alt_binary_search(myList, 9))
print(alt_binary_search(myList, 10))

##--------------------------------------------------------

# binary_search_recursive 

# Borrowed from:
# https://www.codesdope.com/course/algorithms-binary-search/

def binary_search_recursive(a, start, end, x):
  a = sorted(a) # Ensure list is sorted

  # a     --> sorted list
  # start --> starting index
  # end   --> stoping index
  # x     --> item to find

  if (start <= end):
    middle = (start + end)//2
    if (a[middle] == x):
      return middle

    if (a[middle] > x):
      return binary_search_recursive(a, start, middle - 1, x)

    if (a[middle] < x):
      return binary_search_recursive(a, middle + 1, end, x)

  return -1 # not found

##--------------------------------------------------------

if __name__ == '__main__':
  sortedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  indexResult = binary_search_recursive(sortedList, 0, 9, 10)
  print()
  print(sortedList)
  print('Item to find: ', 10)
  print('Results from binary_search_recursive')
  print(indexResult)

  # Imagine passing in an unsorted array/list
  unsortedList = [34, 12, 54, 6, 2, 9, 10, 4, 7, 3]
  indexResult = binary_search_recursive(unsortedList, 0, 8, 9)
  print()
  print(unsortedList)
  print('Item to find: ', 9)
  print(sorted(unsortedList))
  print('Results from binary_search_recursive')
  print(indexResult)

  # Imagine passing in an unsorted array/list
  unsortedList = [34, 12, 54, 6, 2, 9, 10, 4, 7, 3]
  indexResult = binary_search_recursive(unsortedList, 0, 8, 28)
  print()
  print(unsortedList)
  print('Item to find (not in list): ', 28)
  print(sorted(unsortedList))
  print('Results from binary_search_recursive')
  print(indexResult)

##--------------------------------------------------------

