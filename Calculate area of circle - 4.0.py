import time  #  code = time.sleep (1.00["or whatever amount of time you want")
import math  #  this was to import "pi" into the equation  #


#  defining my functions  #
def choices():
                        #  Will always print first  #
    print("\n"*4)
    print ("II                                                 II")
    print ("II=================================================II")
    print ("II=================================================II")
    print ("II------                                     ------II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II               Very basic circle caculations     II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II        What caculation do you wish to do?       II")
    print ("II                      a. area                    II")
    print ("II                      b. circumference           II")
    print ("II                                                 II")
    print ("II                   Make your choice:             II")


def your_number():
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II------                                     ------II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                 Enter radius here:              II")
    

def no_neg():
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                       error...                  II")
    print ("II           No Negative numbers allowed!          II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II------   Press Enter For New Calculation   ------II")
    print ("II------      Press 'Q' To Exit Program      ------II")
    print ("II=================================================II")
    print ("II=================================================II")
    print ("II                                                 II")

    answer_c = input ()

    if answer_c == "q" or answer_c == "Q":
        quit_f()

    else:
        print ("\n" *100)


def to_big():
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                       error...                  II")
    print ("II      Can not compute! To big of a number!       II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II------   Press Enter For New Calculation   ------II")
    print ("II------      Press 'Q' To Exit Program      ------II")
    print ("II=================================================II")
    print ("II=================================================II")
    print ("II                                                 II")

    answer_c = input ()

    if answer_c == "q" or answer_c == "Q":
        quit_f()

    else:
        print ("\n" *100)


def complete():
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II               calculation completed!            II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II                                                 II")
    print ("II------   Press Enter For New Calculation   ------II")
    print ("II------      Press 'Q' To Exit Program      ------II")
    print ("II=================================================II")
    print ("II=================================================II")
    print ("II                                                 II")

    answer_c = input ()

    if answer_c == "q" or answer_c == "Q":
        quit_f()

    else:
        print ("\n"*10)


def quit_f():
    quit()

    
while True:

    try:        

        #  Will always print first  #
        choices()
        answer = input("II                        :")

        #  code beyond this point is for (a) area  #
        if answer == "a":
            your_number()
            r = int(input("II                        :"))

            if (r) > int(0) and (r) < 2001:
                r = (math.pi)*int(r)**2

                print ("II                                                 II")
                print ("II                  Area of circle:                II")
                print ("II                       :",format(r, '.3f') + "u")
                complete()

            elif (r)<0:
                no_neg()

            elif (r) > 2001:
                to_big()

        elif answer == "q" or answer == "Q":
            quit_f()
                
        #  code beyond this point is for (b) circumference  #
                      
        if answer == "b":
            your_number()

            r = int(input("II                        :"))

            if (r) > int(0) and (r) < 2001:
                r = 2*(math.pi)*(r)

                print ("II                                                 II")
                print ("II               Circumfernce of circle:           II")
                print ("II                       :",format(r, '.3f') + "u")
                complete()

            elif (r)<0:
                no_neg()

            elif (r) > 2001:
                to_big()

    except Exception as e:
        print("TypeError:  Pleace input numerical values only")
        time.sleep(2)
