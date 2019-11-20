""" 

##------------------Binary Search------------------

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

##--------------------------------------------------

# Binary Search Algorithm Analysis

Binary Search is a FAST search algorithm.

Suppose we have n items to search through:

Time complexity:
Worst-case:       O(log n)
Best-case:        O(1)
Average-case:     O(log n)

Space complexity:
Worst-case:       O(1)

##--------------------------------------------------

# References:
# https://en.wikipedia.org/wiki/Binary_search_algorithm
# https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm
# https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

"""

##---------I use these lines to visually separate--------- 
##---------code blocks and guide you on which block---------
##---------to comment / uncomment and run as a unit---------

##--------------------------------------------------

# binary_search with comments

def binary_search(sorted_list, target_item):
  sorted_list = sorted(sorted_list) # Ensure list is sorted
  print() # Print new line for readability
  print(sorted_list)

  # Declare start and end indexes in one swoop
  start, end = 0, len(sorted_list) - 1
  
  while start <= end:
    # Always find the new mid-point with every loop
    mid_index = int((start + end ) / 2)
    # Always find the mid value with every loop
    mid_value = sorted_list[mid_index]

    if mid_value == target_item:
      print('Found %d at index %d' %(target_item, mid_index))
      return mid_index
    
    # Item to find is less than value at mid-point
    elif target_item < mid_value:
      end = mid_index - 1

    # Item to find is greater than value at mid-point
    elif target_item > mid_value:
      start = mid_index + 1

  print('Item %d not found!' %target_item)
  return None

##--------------------------------------------------

""" 
# binary_search without comments

def binary_search(sorted_list, target_item):
  sorted_list = sorted(sorted_list)
  print()

  start, end = 0, len(sorted_list) - 1
  
  while start <= end:
    mid_index = int((start + end) / 2)
    mid_value = sorted_list[mid_index]

    if target_item == mid_value:
      return mid_index

    elif target_item < mid_value:
      end = mid_index - 1 

    elif target_item > mid_value:
      start = mid_index + 1

  return None

 """

##--------------------------------------------------

# Try binary_search
print()
print('Results from binary_search')
# my_list contains prime numbers between 1 and 100
my_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

binary_search(my_list, 13)
binary_search(my_list, 37)
binary_search(my_list, 9)
binary_search(my_list, 89)

##--------------------------------------------------

# alt_binary_search without comments

def alt_binary_search(sorted_list, target_item):
  sorted_list = sorted(sorted_list)
  start, end = 0, len(sorted_list) - 1
  print()
  
  while start != end:
    import math
    mid_index = math.ceil((start + end) / 2)   
    
    if target_item < sorted_list[mid_index]:
      end = mid_index - 1
    else: start = mid_index

  if target_item == sorted_list[start]:
    return start

  return None

##--------------------------------------------------

# Try alt_binary_search
print()
my_list = [34, 12, 54, 6, 2, 9, 10, 4, 7, 3]
print(my_list)
print('Results from alt_binary_search')
print(alt_binary_search(my_list, 1))
print(alt_binary_search(my_list, 34))
print(alt_binary_search(my_list, 9))
print(alt_binary_search(my_list, 10))

##--------------------------------------------------


