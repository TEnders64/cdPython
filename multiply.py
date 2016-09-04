
def multiply(arr, b):
    array = []
    for i in arr:    
        array.append(b*i)
    return array

a = [2,4,10,16]    
b = multiply(a, 5)
print b