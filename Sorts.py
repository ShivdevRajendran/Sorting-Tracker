import random
import timeit
import math

def randArray(num):
    arr = list()
    for i in range(0, num):
        x = random.randint(0, 1000) 
        arr.append(x)
    return arr

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def insertionSort(arr):
    for i in range(1, len(arr)):
        currentVal = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] > currentVal):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = currentVal

    return arr

def bubbleSort(arr):
    noSwaps = True
    for i in range(len(arr), 0, -1):
        noSwaps = True
        for j in range(0, i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                noSwaps = False
        if(noSwaps):
            break
    return arr

def selectionSort(arr):
    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    for i in range(0, len(arr)):
        lowest = i
        for j in range(i+1, len(arr)):
            if (arr[lowest] > arr[j]):
                lowest = j
        if (i != lowest): 
            swap(arr, i, lowest)
    return arr

def mergeSort(arr):
    def merge(arr1, arr2):
        results = list()
        i = 0
        j = 0
        while (i < len(arr1)) and (j < len(arr2)):
            if (arr2[j] > arr1[i]):
                results.append(arr1[i])
                i += 1
            elif (arr1[i] > arr2[j]):
                results.append(arr2[j])
                j += 1
            else: #if equal
                results.append(arr1[i]) 
                results.append(arr2[j])
                i += 1
                j += 1
            
        while (i < len(arr1)):
            results.append(arr1[i])
            i += 1
        while (j < len(arr2)):
            results.append(arr2[j])
            j += 1
        return results
    if (len(arr) <= 1): return arr
    mid = math.trunc(len(arr) / 2)
    left = mergeSort( arr[slice( 0, mid )] )
    right = mergeSort( arr[slice( mid, len(arr))] )

    res = merge(left, right)
    return res

def quickSort(arr):
    def pivot(arr):
        start = 0
        pivot = arr[start]
        swapIdx = start
        
        for i in range(start + 1, len(arr)):
            if (pivot > arr[i]):
                swapIdx += 1
                swap(arr, swapIdx, i)
        swap(arr, start, swapIdx)
        return swapIdx
    left = 0
    right = len(arr) - 1
    if (left < right):
        pivotIndex = pivot(arr)
        quickSort(arr[slice(left, pivotIndex - 1)])
        quickSort(arr[slice(pivotIndex + 1, right)])
    return arr

def radixSort(arr):
    def getDigit(num, place):
        digit = (math.trunc(num / (10**place))) % 10
        return digit
    def digitCount(num):
        if (num == 0): return 1
        return math.trunc(math.log10(num)) + 1
    def mostDigits(nums):
        maxDigits = 0
        for i in range(0, len(nums)):
            maxDigits = max(maxDigits, digitCount(nums[i]))
        return maxDigits
    
    maxDig = mostDigits(arr)
    for k in range(0, maxDig):
        digBuckets = 10 * [list()]
        for i in range(0, len(arr)):
            digBuckets[getDigit( arr[i] , k)].append(arr[i]) 
        arr.clear()
        for i in range(0, 10):
            for j in range(0, len(digBuckets[i])):
                arr.append(digBuckets[i][j])
            digBuckets[i].clear()
    return arr

#generates random array
arraySize = int(input("Enter array size: "))
arrayInsert = randArray(arraySize)
arrayBubble = arrayInsert
arraySelection = arrayInsert
arrayMerge = arrayInsert
arrayQuick = arrayInsert
arrayRadix = arrayInsert
print("Generating random array...\n",arrayInsert)

#insertion sort
print("\nInsertion Sort")
start = timeit.default_timer()
print( insertionSort(arrayInsert) )
end = timeit.default_timer()
print("Time Elapsed:", (end - start), "seconds")

#bubble sort
print("\nBubble Sort")
start = timeit.default_timer()
print( bubbleSort(arrayBubble) )
end = timeit.default_timer()
print("Time Elapsed:", (end - start), "seconds")

#selection sort
print("\nSelection Sort")
start = timeit.default_timer()
print( selectionSort(arraySelection) )
end = timeit.default_timer()
print("Time Elapsed:", (end - start), "seconds")

#merge sort
print("\nMerge Sort")
start = timeit.default_timer()
print( mergeSort(arrayMerge) )
end = timeit.default_timer()
print("Time Elapsed:", (end - start), "seconds")


#radix sort
print("\nRadix Sort")
start = timeit.default_timer()
print( radixSort(arrayRadix) )
end = timeit.default_timer()
print("Time Elapsed:", (end - start), "seconds")

#quick sort
print("\nQuick Sort")
start = timeit.default_timer()
try:
    print( quickSort(arrayQuick) )
except:
    print("FAILED - Too much recursion has occured in one run of this file... Sorry")
end = timeit.default_timer()
print("Time Elapsed:", (end - start), "seconds")


