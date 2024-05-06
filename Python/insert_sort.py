import os 

arr = [4,5,2,5,7,8,910,200]

print(arr)

def insert_sort():
    for j in range(1, len(arr)):
        actual = arr[j]
        print("valor actual", actual, " Posicion ", j)
        i = j-1
        print("condicion: valor de i:", i, " valor arr[i]:", arr[i] , " Valor de actual:", actual)
        os.system('cls')
        while i >= 0 and arr[i] > actual:
            arr[i+1] = arr[i]
            i -=1
    arr[i+1] = actual
    print("posicion", i+1 , " actual ", actual)

print(arr)


def call_insert():
    pass