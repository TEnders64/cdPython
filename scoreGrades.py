def scoreGrades():
    i = 0
    print "Scores and Grades"
    while(i < 11):
        try:
            score = int(raw_input("Score: "))    
            if (1 <= score <= 100):
                if(1 <= score <= 59):
                    print "Score: " + str(score) + "; Your grade is F"
                    i=i+1
                if(60 <= score <= 69):
                    print "Score: " + str(score) + "; Your grade is D"
                    i=i+1
                if(70 <= score <= 79):
                    print "Score: " + str(score) + "; Your grade is C"
                    i=i+1
                if(80 <= score <= 89):
                    print "Score: " + str(score) + "; Your grade is B"
                    i=i+1
                if(90 <= score <= 100):
                    print "Score: " + str(score) + "; Your grade is A"
                    i=i+1
            else:
                print "Please enter a score between 1 and 100"
        except: 
            ValueError
            print "That is not a number. Please enter a score between 1 and 100"
            
    print "End of the program. Bye!"
    
scoreGrades()