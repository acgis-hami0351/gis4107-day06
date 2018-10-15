#-------------------------------------------------------------------------------
# Name:        GuessCounter.py
# Purpose:
#
# Author:      Nick and Ryan
#
# Created:     15/10/2018
# Copyright:
# Licence:
#-------------------------------------------------------------------------------

import random
reload(random)

import numpy
reload(numpy)

def main():
    guessList = []
    for calls in range(10):
        result = get_guess_count(7,0,1000)
        print result
        guessList.append(result)
    print "Average of 10 guesses: {}".format(numpy.mean(guessList))
    print "Minimum of 10 guesses: {}".format(min(guessList))
    print "Maximum of 10 guesses: {}".format(max(guessList))

def get_guess_count (number_to_guess, min_bound, max_bound):
    if (number_to_guess < min_bound) or (number_to_guess > max_bound):
        return 0
    guess = random.randint(min_bound,max_bound)
    counter = 0
    if guess == number_to_guess:
        return counter
    while guess != number_to_guess:
        guess = random.randint(min_bound,max_bound)
        if guess == number_to_guess:
            return counter
        else:
            counter += 1
            if guess > number_to_guess:
                max_bound -= 1
            if guess < number_to_guess:
                min_bound += 1
            if counter > 100000:
                break

def test_get_guess_count():
    print get_guess_count(7,0,1000)

if __name__ == '__main__':
    main()
