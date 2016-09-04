
def oddEven(start, end):
    for i in range(start, end):
        if i % 2 != 0:
            print "Number is " + str(i) + '. This is an odd number'
        if i % 2 == 0:
            print "Number is " + str(i) + '. This is an even number'
        
oddEven(1, 2001)