def lose():
    import sys
    import time
    print '''

 _____                        _____                
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
                                                  Maximilian has won!

                       u mad?                                 
    '''

    time.sleep(4)

    sys.exit("beep! errors! QQ + rage bye!")
    time.sleep(4)


def function():
    #importing the time module
    import time
    

    #welcoming the user
    name = raw_input("TYPE YO NAME!\n\n")

    print "Hello, " + name, "its time... to play a guessing game!"

    print "\n"

    #wait for 1 second
    time.sleep(1)

    print "Start guessing..."
    time.sleep(0.5)

    #here we set the secret
    word = "hipster"

    #creates an variable with an empty value
    guesses = ''

    #determine the number of turns
    turns = 5

    # Create a while loop

    #check if the turns are more than zero
    while turns > 0:         

        # make a counter that starts with zero
        failed = 0             

        # for every character in secret_word    
        for char in word:      

        # see if the character is in the players guess
            if char in guesses:    
        
            # print then out the character
                print char,    

            else:
        
            # if not found, print a dash
                print "_",     
           
            # and increase the failed counter with one
                failed += 1    

        # if failed is equal to zero

        # print You Won
        if failed == 0:        
            print "\nYou won"  

        # exit the script
            break              

        print

        # ask the user go guess a character
        guess = raw_input("guess a character:") 

        # set the players guess to guesses
        guesses += guess                    

        # if the guess is not found in the secret word
        if guess not in word:  
     
         # turns counter decreases with 1 (now 9)
            turns -= 1        
     
        # print wrong
            print "Wrong\n"    
     
        # how many turns are left
            print "You have", + turns, 'more guesses' 
     
        # if the turns are equal to zero
            if turns == 0:           
                
            # print "You Loose"
                print "You Loose\n" 
                print lose()

    #             import random
    # print random.function()
                 