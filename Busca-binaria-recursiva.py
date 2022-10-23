def busca_recursiva(arr,numb,end = None, start = 0):
    if end is None:
        end = len(arr)-1
    if start>end:
        return False
    
    meio = (start + end) // 2 #meio = mid
    if numb == arr[meio]:
        return meio
    if numb < arr[meio]:
        return busca_recursiva(arr, numb, meio-1 , start)
    return busca_recursiva(arr, numb, end, meio+1)