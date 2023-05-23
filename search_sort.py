# Schyler Lowry
# 1-27-2023
# CRN: 23199
# CIS 226: Advanced Python Programming
# Time Spent: 11ish hours
# Day 1: 3hr15min
# Day 2: 3hr30min
# Day 3: 4hr15min

"""
This program takes the example data in global var 'EXDATA' and turns it into a linked list. 
The program performs a selection sort, and prints the sorted list.
The program performs a linear, and a binary search respectively. It then prints the list with the index position of the searched value.
"""
# EDITED ON 4-21-23: Altered the traverse_linked function to accept a parameter to search for
#                    the function now traverses the linked list until it finds the the search parameter
#                    it also returns the position of the link

# Caveats: it doesn't handle errors if the search parameter is not found in the linked list 

class Node:
    """This class contains the functions that turn data into nodes for a linked list"""
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext


def array_to_linked(arr):
    """
    Pass in an array. Index 0 of the array is instantiated as a node, with var name: temp. 
    The array is then iterated for its length, and at each iteration it calls the set_next method from the Node class to assign the next object in the linked list
    """
    temp = Node(arr[0])
    head = temp
    i = 1
    while i!= len(arr):
        nextnode = Node(arr[i])            
        temp.set_next(nextnode)
        temp = nextnode
        i += 1        
    return head



def traverse_linked(head, search):
    """
    Function for traversing, and then printing the linked list.
    The linked list is iterated until the value for the search parameter is reached.
    """
    # O(n)
    links = 0
    temp = head

    while temp.get_data() != search:
        print("{} ===> ".format(temp.get_data()),end='')
        temp = temp.get_next()
        links += 1
    print("{} ===> ".format(temp.get_data()))
    print("The value {} is found at link {}.".format(search, links))

def selection_sort(arr):
    """
    Pass in array to be sorted.
    The function iterates for the length of the array -1. It checks each value in the array agains the value of 'first_marker'.
    The 'swap' function is called, when the value of the first marker is not equal to that of the third marker.
    """
    # O(n^2)
    times_swapped = 0
    for first_marker in range(len(arr) - 1):
        third_marker = first_marker
        for second_marker in range(first_marker+1, len(arr)):
            if arr[second_marker] < arr[third_marker]:
                third_marker = second_marker
        if first_marker != third_marker:        
            swap(arr, third_marker, first_marker)
            times_swapped += 1  
    print("times swapped:", times_swapped)
    
def swap(A, x, y):
    """
    Updates array based on the parameters given from the selectionSort function
    """
    # O(1)
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


def linear_search(arr, look_for):
    """
    The array gets searched, starting at index 0. With each iteration, if the request search value was not found, the starting index increases until it's found.
    """
    # Steps: 16ish?
    # O(n)
    index = 0
    for i in arr:
        if i == look_for:
            return index
        else:
            index +=1
    return "Not found"

def binary_search(arr, look_for): 
    """
    The array is split down the middle and the two halves are searched. It continues cutting the array in half until it finds the requested value.
    The middle is determined by dividing the length of the array in two. 
    If the search value is larger than that of the middle value, then it searches the right half, and vice versa.
    """
    # Steps: 4ish?
    # O(log n)
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == look_for:
            return mid   
        elif arr[mid] < look_for:
            start = mid+1
        else:
            end = mid-1
    return "Not found"

EXDATA = [1, 7, 4, 2, 9, 8, 10, -4, 0, 3]



def main():
    # creates the linked list
    head = array_to_linked(EXDATA)
    print("================================\nLinked list - Unsorted:")
    traverse_linked(head,8)
    print("\n================================")

    # uses selection sort to sort the example data
    sortedlist = EXDATA.copy()
    selection_sort(sortedlist)
    print("Selection sorted list:\n",sortedlist)
    print("================================")

    # performs linear search on unsorted example data
    mylist2 = EXDATA.copy()
    index = linear_search(mylist2, 8)
    print("Linear Search:")
    print("The value {} is at index {}".format(8, index))
    print(mylist2)
    print("================================")

    # performs binary search on sorted example data
    index = binary_search(sortedlist, 8)
    print("Binary Search:")
    print("The value {} is at index {}".format(8, index))
    print(sortedlist)
    print("================================")
    

if __name__ == "__main__":
    main()



def test_arr_to_linked():
    """
    Checks to see that the data returned from the array_to_linked function is the same as the data in the first index of the passed in array.
    """
    originalarr = ["a","b","c"]
    checkedlist = array_to_linked(["a","b","c"])
    print(checkedlist.get_data())
    assert originalarr[0] == checkedlist.get_data()

def test_search():
    """
    Checks to see that the returned index value of the two search functions is the same as what we expect.
    Also checks to see if the function returns 'Not found', in the event of the searched number not being contained in the passed-in array.
    """
    sortedlist = [-4, 0, 1, 2, 3, 4, 7, 8, 9, 10]
    numbertofind = 8
    expectedindex = 7
    numbertoNotfind = -5
    assert binary_search(sortedlist, numbertofind) == expectedindex
    assert binary_search(sortedlist, numbertoNotfind) == "Not found"
    assert linear_search(sortedlist, numbertofind) == expectedindex
    assert linear_search(sortedlist, numbertoNotfind) == "Not found"
    