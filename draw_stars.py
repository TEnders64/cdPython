
def draw_stars(arr):
    for i in arr:
        if (type(i) == int):
            print(i*'*')
        else:
            print (len(i) * i[0]).lower()
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)