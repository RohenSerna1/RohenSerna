def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

lista = [5,1,4,2,8]
print("Lista original:", lista)
bubble_sort(lista)
print("Lista ordenada:", lista)