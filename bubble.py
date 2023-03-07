""" num = [4, 3, 7, 1, 5]
def bubble_sort(num):
    swapped = False
    for n in range(len(num)-1,0,-1):
        for i in range(n):
            if num[i] > num[i+1]:
                swapped = True
                num[i], num[i+1] = num[i+1], num[i]
        #print(num) # look what happening
        if not swapped:
            return
        
print("Unsorted list is,")
print(num)
bubble_sort(num)
print("Sorted Array is, ")
print(num)

def bub_s(L):
    l = len(L)
    for i in range(l-1):
        flag = False
        for j in range(l-1-i):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                flag = True
        #print(L) # look what happening
        if flag == False:
            break
    return L
print(f'{bub_s([1,2,3,4])}')

def bubble_sort(my_list):
  list_length = len(my_list)
  is_sorted = False # wrong initialization
  while not is_sorted: 
    is_sorted = True
    for i in range(list_length-1):
      if my_list[i] > my_list[i+1]: # wrong condition
        my_list[i] , my_list[i+1] = my_list[i+1] , my_list[i]
        is_sorted = False
    list_length -= 1 # updating the length of the list
  return my_list

print(bubble_sort([5, 7, 9, 1, 4, 2]))


# Merge Sort
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)


def merge_sort(L):
    if len(L) > 1:
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1
        
        while len(left) > i:
            L[k] = left[i]
            i += 1
            k += 1
        while len(right) > j:
            L[k] = right[j]
            j += 1
            k += 1
            
out_list = [10,90,1,56,25,75,81,15,9]
merge_sort(out_list)
print(out_list)

# Task 6
def merge_sort(my_list):
    if len(my_list) > 1: 
        mid = len(my_list)//2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]                
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1

my_list = [35,22,90,4,50,20,30,40,1]
merge_sort(my_list)
print(my_list) """


# Recursive Func #
num_list = [2,10,8,30]

def addition(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + addition(lst[1:])
    
print(addition(num_list))
print()

rev_func = lambda l:(rev_func(l[1:]) + l[:1] if l else [])

print(rev_func(num_list))
print()

movie = 'The Last of Us'
def rev_str(s):
    if len(s) == 0:
        return s
    else:
        return rev_str(s[1:]) + s[0]
print(rev_str(movie))
print()

def fact_fun(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact_fun(num - 1)
    
print(fact_fun(5))
print()

# Fibonacci recurcive #
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))