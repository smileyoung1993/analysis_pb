import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
from matplotlib import font_manager, rc


def ex1():
    plt.plot([1,2,3,4],[10,30,20,40])

    plt.show()

def ex2():
    fig = plt.figure()
    sp1 = fig.add_subplot(2,1,2)
    sp1.plot([1,2,3,4],[10,30,20,40])

    plt.show()

def ex3():
    fig = plt.figure()
    sp1 = fig.add_subplot(1, 2, 1)
    sp1.plot([1, 2, 3, 4], [10, 30, 20, 40])

    sp2 = fig.add_subplot(1, 2, 2)
    sp2.plot([1, 2, 3, 4], [10, 30, 20, 40])

    plt.show()

def ex4():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(randn(50).cumsum(),'k--') # cumsum??

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(randn(100),bins=20,color='k',alpha=0.3)

    sp3 = fig.add_subplot(2,2,3)
    sp3.scatter(np.arange(100),np.arange(100)+3*randn(100))

    plt.show()

def ex5():
    fig, subplots = plt.subplots(2,2)

    print(subplots)

    plt.show()

def ex6():

    fig, subplots = plt.subplots(2, 2, sharex=True, sharey=True)
    for i in range(2):
        for j in range(2):
            subplots[i,j].hist(randn(100), bins=20, color='k', alpha=0.3)

    plt.subplots_adjust(wspace=0, hspace=0)

    plt.show()

def ex7():
    fig, subplots = plt.subplots(1,1)
    subplots.plot([10,20,30,40])
    plt.show()

def ex8():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([1,2,3,4],[10, 20, 30, 40],'go--')
    plt.show()

def ex9():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([1,2,3,4],[10, 20, 30, 40],color = 'g',linestyle='--',marker='o')
    plt.show()

def ex9():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([1,2,3,4],[10, 20, 30, 40],color = 'g',linestyle='--',marker='o')
    plt.show()

def ex10():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot(randn(50).cumsum(),'ko--')

    plt.show()

def ex11():
    data = randn(50).cumsum()

    fig, subplots = plt.subplots(1,1)
    subplots.plot(data, color = 'g',linestyle = '--', label = 'Default')
    subplots.plot(data, 'k-', drawstyle = 'steps-mid', label = 'steps-mid')

    plt.legend(loc = 'best')
    plt.show()

if __name__ == '__main__':
    #ex1()
    #ex2()
    #ex3()
    #ex4()
    #ex5()
    #ex6()
    #ex7()
    #ex8()
    #ex9()
    #ex10()
    ex11()