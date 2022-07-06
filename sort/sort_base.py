import numpy as np
import abc
# import matplotlib.pyplot as plt

class BaseSort:
    '''Base class for sorting algorithm classes. 
       Derived classes have to implement sort() and sortingStep_gen() methods.
       Use val() & cmp() methods to access/compare elements (so that counters increments properly)
    '''

    def __init__(self, data, sortInSteps):
        self.data = np.array(data)
        self.N = self.data.size
        self.inSteps = sortInSteps
        self.sorted = False
        self.cc = 0     #comparison counter
        self.ca = 0     #array access counter
        self.horLine = -100     #optional position of a horizontal line

        #variables for element coloring (value can be int or list of ints; negative means unset)
        self.anc = {'darkgray': -1, 'mediumaquamarine': -1, 'salmon': -1, 'skyblue': -1, 'g': -1, 'y': -1, 'orchid':-1, 'r': -1}

        #init generator, if drawing is enabled
        if sortInSteps:
            self.sortingStep = self.sortingStep_gen()

    def stepGen(self):
        self.sorted = False
        i = 0
        while not self.sorted:
            i += 1
            yield i
            # plt.savefig(f'anim/frame_{i}.png')
        # plt.savefig(f'anim/frame_{i+1}.png')
    
    def crst(self):
        self.ca = self.cc = 0
    
    def cmp(self, i, j):
        self.ca += 2
        self.cc += 1
        return self.data[i] < self.data[j]
    
    def cmp2(self, val, i):
        self.ca += 1
        self.cc += 1
        return val < self.data[i]
    
    def __getitem__(self, i):
        self.ca += 1
        return self.data[i]

    def swap(self, i, j):
        self.ca += 2
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp

    @abc.abstractmethod
    def sort(self):
        '''Regular sorting algorithm implemenentation'''
        raise NotImplementedError("Algorithm needs to implement sorting methods")

    @abc.abstractmethod
    def sortingStep_gen(self):
        '''Step generator, used when drawing results step by step'''
        raise NotImplementedError("Algorithm needs to implement sorting methods")

    def update(self):
        if self.inSteps:
            next(self.sortingStep)
        else:
            self.sort()
            self.sorted = True