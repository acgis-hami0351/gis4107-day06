import numpy, random


##number_to_guess = randint(10, 95)

min_bound = 1
max_bound = 10000

def get_guess_count(number_to_guess, min_bound, max_bound):
    if min_bound >= number_to_guess or  max_bound < number_to_guess:   # need to eval both sides should use the or, need to just eval left to right use and
        return 0
    else: #start counter once the above statement is true
        theSum = 0
        while number_to_guess != theSum:
            ranNum = random.randint (min_bound, max_bound)
            if ranNum != number_to_guess:
                theSum += 1
                if theSum >= 100000:
                    break
        return theSum

def main():
    mylist = []
    for i in range(10):
        guess = random.randint (1, 10000)
        guessCount = get_guess_count(guess, min_bound, max_bound)
        print guessCount
        mylist.append(guessCount)
    print mylist
    print '{} this is the min'.format (min (mylist))
    print '{} this is the max'.format (max (mylist))



if __name__ == '__main__':
    main()
