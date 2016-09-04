import random

def coinFlip(numberOfFlips):
    heads = 0
    tails = 0
    count = 0
    for i in range(1, numberOfFlips+1):
        random_num = round(random.random())
        if (random_num == 1):
            heads += 1
            count += 1
            print ("Attempt #%s. Throwing a coin... It's heads! ... Got %s head(s) so far and %s tail(s) so far" % (count, heads, tails)) 
        if (random_num == 0):
            tails += 1
            count += 1
            print ("Attemp $%s. Throwing a coin... It's tails! ... Got %s head(s) so far and %s tail(s) so far" % (count, heads, tails)) 
        if (count == numberOfFlips):
            print "End of Program!"
coinFlip(5000)