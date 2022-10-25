#Bubble sort
def bubble(arr):
    f = True
    while f == True:
        k = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                s = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = s
                k +=1
        if k == 0:
            f = False
    return arr
#testing
a =[1,5,0,2,3,4,15,12,70,12,96,12,45,61,2,0,12,45,65]
print(bubble(a))

#Selection sort
def selection(arr):
    for i in range(len(arr)):
        menor = i
        for j in range(len(arr)):
            if j > i:
                if arr[j] < arr[menor]:
                    menor = j
        if arr[i] != arr[menor]:
            s = arr[menor]
            arr[menor] = arr[i]
            arr[i] = s
    return arr
print(selection(a))

#insertion sort
