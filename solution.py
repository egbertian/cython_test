# https://www.peterbaumgartner.com/blog/intro-to-just-enough-cython-to-be-useful/

# use python 3.12
# use setuptools instead of distutils_core


import random, time


def calc_lists(n_values):
    t0 = time.time()

    list1 = []
    list2 = []

    result_list = []

    for i in range(n_values):
        list1.append(random.randint(1,10))
        list2.append(random.randint(1,10))

    for x1 in list1:
        for x2 in list2:
            result_list.append(x1*x2)


    my_max = max(result_list)    
    my_mean = sum(result_list)/len(result_list)
    t1 = time.time()
    deltaT = t1-t0

    print(f"max = {my_max}")
    print(f"mean = {my_mean}")
    print(f"t = {deltaT}")

    return (my_max, my_mean, deltaT)

# calc_lists(8000)