
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # initialize as min item in list
        min = i

        for j in range(i+1, n):
            if (arr[j] < arr[min]):
            # update pos if item is lesser than the prev item
                min = j

        # swap them
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        guard_clause = 0
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                guard_clause = 1
                if guard_clause == 0:
                    break
    arr = arr[::-1] # ascending order
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
  
        temp = arr[i]
  
        # Shift elements of array[0 to i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and temp < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = temp
    return arr


def merge_sort(nlist):
    if len(nlist) > 1:
        mid = len(nlist) // 2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = j = k = 0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k] = lefthalf[i]
                i = i+1
            else:
                nlist[k]=righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    return nlist


def print_test():
    """testing the sorting algo"""
    
    array = [11, 4, 3, 6, 1, 19, 10]
    print("Orig: ", array, "\n", "List sorted with selection_sort in descending order: ", selection_sort(array))

    array = [5, 3, 4, 1, 2]
    print("Orig: ", array, "\n", "List sorted with bubble sort in ascending order: ", bubble_sort(array))

    array = [5, 3, 4, 8, 7]
    print("Orig: ", array, "\n", "List sorted with insertion sort in ascending order: ", insertion_sort(array))
    
    array = [11, 4, 3, 6, 1, 19, 10]
    print("Orig: ", array, "\n", "List sorted with merge_sort in ascending order: ", merge_sort(array))


if __name__ == "__main__":
    print_test()

