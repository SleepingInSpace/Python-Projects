# This function swaps the elements of arr(array/list) present at index i and index j
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# This function places the pivot element at its place 
#and returns the index of the pivot element
def divide(arr, start, end):
    # pivot is selected as the first element of the array/list
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end: # update the start until element greater than pivot is found
        while start < len(arr) and arr[start] <= pivot :
            start += 1 
        while arr[end] > pivot: # update the end until element smaller than pivot is found 
            end -= 1 
        if start < end:
             # swapping the element at index start with element at index end,
             # so that elemnts greater than pivot can be placed on right side and smaller can be
             # placed left side of pivot element
            swap(arr, start, end)
           
    swap(arr, pivot_index, end) # swapping the pivot to its sorted position 
    print(arr)
    print("pivot:",pivot_index)
    print("start:",start)
    print("end:",end)
    return end
def quickSort(arr, start,end):
    if start < end:
        pivot_index = divide(arr, start, end)
        quickSort(arr, start, pivot_index -1)
        quickSort(arr, pivot_index+1, end)
        

if __name__ == "__main__":
    list = [4,4,4,4]
    
    quickSort(list, 0, len(list) -1)