a = [1, 2, 5, 10, 255, 3]

def avgList(arr):
    sum_a = 0
    for i in a:
        sum_a += i
    sum_a = sum_a / len(arr)
    print sum_a
    
avgList(a)