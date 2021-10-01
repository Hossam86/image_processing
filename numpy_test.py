import time
import numpy as np


def sum_with_loop():
    no_of_terms = 10000000
    # Calculate the denominator.
    # First Few terms are 1, 3, 5, 7 ...
    den = np.linspace(1, no_of_terms*2, no_of_terms)

    # Calculate the numerator
    # The first few terms are 1, -1, 1
    num = np.ones(no_of_terms)
    for i in range(1, no_of_terms):
        num[i] = pow(-1, i)

    counter = 0
    sum_value = 0

    t1 = time.process_time()
    while counter < no_of_terms:
        sum_value += (num[counter]/den[counter])
        counter = counter+1
    pi_value = sum_value*4.0
    print("pi_value is:%f" % pi_value)
    t2=time.process_time()
    # Determine the time for the compution
    timetaken=t2-t1
    print("Time taken is: %f seconds" % timetaken)

def sum_with_numpy():
    no_of_terms = 10000000
    # Calculate the denominator.
    # First Few terms are 1, 3, 5, 7 ...
    den = np.linspace(1, no_of_terms*2, no_of_terms)

    # Calculate the numerator
    # The first few terms are 1, -1, 1
    num = np.ones(no_of_terms)
    for i in range(1, no_of_terms):
        num[i] = pow(-1, i)

    t1 = time.process_time()
    
    pi_value = sum(num/den)*4.0

    print("pi_value is:%f" % pi_value)
    t2=time.process_time()
    # Determine the time for the compution
    timetaken=t2-t1
    print("Time taken is: %f seconds" % timetaken)


if __name__=='__main__':
    sum_with_loop()
    sum_with_numpy()