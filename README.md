# SearchAndSort
Assignment for my Advanced Python class. Program performs various search and sort functions with lists, and linked lists.
This program takes the example data in global var 'EXDATA' and turns it into a linked list. 
The program performs a selection sort, and prints the sorted list.
The program performs a linear, and a binary search respectively. It then prints the list with the index position of the searched value.
"""
EDITED ON 4-21-23: Altered the traverse_linked function to accept a parameter to search for
                   the function now traverses the linked list until it finds the the search parameter
                   it also returns the position of the link

Caveats: it doesn't handle errors if the search parameter is not found in the linked list 
