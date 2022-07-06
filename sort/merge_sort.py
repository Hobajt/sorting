from numpy.lib.function_base import insert
from .sort_base import BaseSort
import numpy as np

class MergeSort(BaseSort):
    def __init__(self, *argv):
        BaseSort.__init__(self, *argv)
        pass

    def sort(self):
        def insertSort(start, end):
            for i in range(start+1, end, 1):
                val = self[i]
                j = i-1
                while j >= 0 and val < self[j]:
                    self.data[j+1] = self.data[j]
                    self.ca += 1
                    self.cc += 1
                    j -= 1
                self.ca += 1
                self.cc += 1
                self.data[j+1] = val
            pass
        
        def merge(start, end):
            '''Memory allocation is done terribly'''
            a = start
            half = (end - start)//2
            b = start + half

            tmp = np.zeros((end-start))
            va = self[a]
            vb = self[b]
            i = 0
            while a < half and b < end:
                if self[a] < self[b]:
                    tmp[i] = self[a]
                    a += 1
                else:
                    tmp[i] = self[b]
                    b += 1
                i += 1
            while a < half:
                tmp[i] = self[a]
                a += 1
                i += 1
            while b < end:
                tmp[i] = self[b]
                b += 1
                i += 1
            self.data[start:end] = tmp[:]
        
        #generate binary tree of ranges for each partition
        tree = [(0, self.N,)]
        i = 0
        while i < len(tree):
            start, end = tree[i]
            gap = end - start
            i += 1

            if gap < 10:
                insertSort(start, end)
            else:
                gap = gap // 2
                tree.append((start, start+gap,))
                tree.append((start+gap, end,))

        print(len(tree[1:]))
        # #do the sorting/merging within each partition
        # for start,end in tree[::-1]:
        #     gap = end - start

        #     if gap < 10:
                
        #     else:
        #         merge(start, end)


        self.sorted = True
    
    def sortingStep_gen(self):
        # self.anc = dict.fromkeys(self.anc, -1)
        # self.anc['r'] = i
        yield
        self.sorted = True