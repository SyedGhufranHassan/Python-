import sys
def selection_sort(arr):
    for i in range(len(arr)):
        min=i

        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j

        arr[i],arr[min]=arr[min],arr[i]
    return arr
arr=[50,80,40,35,90,12]
a=selection_sort(arr)
for i in range(len(a)):
    print(a[i], end=",")
