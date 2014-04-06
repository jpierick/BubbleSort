import cProfile
import random

__author__ = 'jeff'

# The length of the list that will be generated with random numbers:
list_length = 15000
mylist = []

# Generate a completely random list of numbers:
# for i in range(list_length):
#     mylist.append(random.randrange(32000))

# Generate a perfectly sorted list of numbers:
# for i in range(list_length):
#     mylist.append(i)

# Generate a completely reverse sorted list of numbers:
for i in range(list_length,0,-1):
    mylist.append(i)

def bubble_sort(list):
    sorted = False  # Start by assuming that the list is not sorted.

    # Capture the length of the list just once.  This will save us time by not having to recalculate it
    # every time we go through the following loop:
    list_length = len(list) -1

    while not sorted:
        # We'll start the loop by assuming that the list is sorted.  If we find a pair out of sequence,
        # then we'll track that the list is not sorted.
        sorted = True

        for i in range(list_length):
            # If the current item is greater than the following item, then switch the items and track
            # that the list is not sorted:
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False

print mylist
cProfile.run('bubble_sort(mylist)')
print mylist
