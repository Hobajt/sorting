from .sort_base import BaseSort
import numpy as np
import random

class QuickSort(BaseSort):

    def __init__(self, *argv):
        self.sortingStep_gen = self.sortingStep_gen_arrAvg
        # self.sortingStep_gen = self.sortingStep_gen_randomPivot

        BaseSort.__init__(self, *argv)
        pass

    def quicksort(self, n, data):
        '''Recursive implementation'''
        if n <= 1:
            return data
        
        # pidx = np.random.randint(n)
        pidx = random.randint(n)
        pv = data[pidx]
        lt = []
        gt = []
        self.ca += 1
        for i in range(n):
            if i == pidx:
                continue
            self.cc += 1
            self.ca += 2
            if data[i] < pv:
                lt.append(data[i])
            else:
                gt.append(data[i])

        return [*self.quicksort(len(lt), lt), pv, *self.quicksort(len(gt), gt)]

    def insertSort(self, arr):
        ca = 0
        cc = 0
        for i in range(1, arr.size):
            val = arr[i]
            ca += 2
            cc += 1
            j = i-1
            while j >= 0 and val < arr[j]:
                ca += 1
                arr[j+1] = arr[j]
                j -= 1
            ca += 1
            arr[j+1] = val
        return ca,cc

    def sort(self):
        '''Non recursive implementation.
           Pivot is array average (average of first+last+mid and random are also implemented, but they're commented out).
        '''
        def organize(start, end, pivot):
            '''Sort elements with respect to pivot. Returns of the first element greater than pivot.'''
            a = start
            b = end - 1
            low = 0
            high = 0
            
            while a <= b:
                self.cc += 1
                if self[a] >= pivot:
                    tmp = self.data[a]
                    self.data[a] = self.data[b]
                    self.data[b] = tmp
                    self.ca += 2
                    high += self.data[b]
                    b -= 1
                else:
                    low += self.data[a]
                    a += 1
            return a,low,high


        #take the average of first,last and central element as the first pivot
        pivot = (self.data[0] + self.data[-1] + self.data[self.data.size//2]) / 3
        pivotTree = [(0,self.N,pivot,)]

        # pivotTree = [(0,self.N,self.data[random.randint(0,self.N-1)],)]

        i = 0
        while i < len(pivotTree):
            start,end,pivot = pivotTree[i]
            i += 1

            if end - start <= 10:
            # if end - start <= 3:
                #use insert sort for small enough array
                ca,cc = self.insertSort(self.data[start:end])
                self.ca += ca
                self.cc += cc
            else:
                #else split into two subarrays -> smaller/greater than pivot
                border,lo,hi = organize(start, end, pivot)

                #add entries to the tree, for further processing
                if border > start:
                    pivot = (lo / (border-start)) if ((border-start) > 10) else ((self.data[start] + self.data[border-1] + self.data[start+(border-1-start)//2])*0.333)
                    # pivot = (self.data[start] + self.data[border-1] + self.data[start+(border-1-start)//2])*0.333
                    # pivot = self.data[random.randint(start, border-1)]
                    pivotTree.append( (start, border, pivot,) )
                if border < end:
                    pivot = (hi / (end-border)) if ((end-border) > 10) else ((self.data[border] + self.data[end-1] + self.data[border+(end-1-border)//2])*0.333)
                    # pivot = (self.data[border] + self.data[end-1] + self.data[border+(end-1-border)//2])*0.333
                    # pivot = self.data[random.randint(border, end-1)]
                    pivotTree.append( (border, end, pivot,) )


        self.sorted = True
    
    def sortingStep_gen_randomPivot(self):
        self.anc = dict.fromkeys(self.anc, -1)
        self.anc['g'] = []

        def organize(start, end, pivot, pidx):
            '''Sort elements with respect to pivot. Returns of the first element greater than pivot.'''
            a = start
            b = end - 1
            self.anc['salmon'] = []
            self.anc['skyblue'] = []
            self.anc['r'] = pidx
            self.anc['darkgray'] = list(range(a,b+1))
            
            while a <= b:
                self.anc['y'] = a
                yield -1
                self.cc += 1
                if self[a] >= pivot:
                    tmp = self.data[a]
                    self.data[a] = self.data[b]
                    self.data[b] = tmp
                    self.ca += 2
                    self.anc['y'] = b
                    self.anc['salmon'].append(b)
                    if a == pidx:
                        pidx = b
                        self.anc['r'] = pidx
                    elif b == pidx:
                        pidx = a
                        self.anc['r'] = pidx
                    b -= 1
                    yield -1
                else:
                    self.anc['skyblue'].append(a)
                    a += 1
                    yield -1
            self.anc['darkgray'] = -1
            self.anc['salmon'] = self.anc['skyblue'] = -1
            yield a


        pidx = random.randint(0,self.N-1)
        pivotTree = [(0,self.N,pidx,self.data[pidx],)]

        i = 0
        while i < len(pivotTree):
            start,end,pidx,pivot = pivotTree[i]
            i += 1

            if end - start <= 10:
                #use insert sort for small enough array
                arr = self.data[start:end]
                self.anc['mediumaquamarine'] = [start]
                self.anc['y'] = -1
                for k in range(1, arr.size):
                    val = arr[k]
                    self.anc['r'] = -1
                    self.anc['mediumaquamarine'].append(start+k)
                    self.ca += 2
                    self.cc += 1
                    j = k-1
                    yield
                    while j >= 0 and val < arr[j]:
                        self.ca += 1
                        arr[j+1] = arr[j]
                        self.anc['r'] = start+j
                        j -= 1
                        yield
                    self.ca += 1
                    arr[j+1] = val
                self.anc['g'].extend(self.anc['mediumaquamarine'])
                self.anc['mediumaquamarine'] = -1
                yield
            else:
                #else split into two subarrays -> smaller/greater than pivot
                org = organize(start, end, pivot, pidx)
                border = -1
                while border < 0:
                    border = next(org)
                    yield

                #add entries to the tree, for further processing
                if border > start:
                    pidx = random.randint(start, border-1)
                    pivotTree.append( (start, border, pidx, self.data[pidx],) )
                if border < end:
                    pidx = random.randint(border, end-1)
                    pivotTree.append( (border, end, pidx, self.data[pidx],) )
        

        yield
        self.sorted = True
    
    def sortingStep_gen_arrAvg(self):
        self.anc = dict.fromkeys(self.anc, -1)
        self.anc['g'] = []

        def organize(start, end, pivot):
            '''Sort elements with respect to pivot. Returns of the first element greater than pivot.'''
            a = start
            b = end - 1
            self.anc['salmon'] = []
            self.anc['skyblue'] = []
            self.anc['darkgray'] = list(range(a,b+1))
            lo = hi = 0
            
            while a <= b:
                self.anc['y'] = a
                yield -1
                self.cc += 1
                if self[a] >= pivot:
                    tmp = self.data[a]
                    self.data[a] = self.data[b]
                    self.data[b] = tmp
                    self.ca += 2
                    self.anc['y'] = b
                    self.anc['salmon'].append(b)
                    hi += self.data[b]
                    b -= 1
                    yield -1
                else:
                    self.anc['skyblue'].append(a)
                    lo += self.data[a]
                    a += 1
                    yield -1
            self.anc['darkgray'] = -1
            self.anc['salmon'] = self.anc['skyblue'] = -1
            yield a,lo,hi


        #take the average of first,last and central element as the first pivot
        pivot = (self.data[0] + self.data[-1] + self.data[self.data.size//2]) / 3
        pivotTree = [(0,self.N,pivot,)]

        i = 0
        while i < len(pivotTree):
            start,end,pivot = pivotTree[i]
            i += 1

            if end - start <= 10:
                self.horLine = -1

                #use insert sort for small enough array
                arr = self.data[start:end]
                self.anc['mediumaquamarine'] = [start]
                self.anc['y'] = -1
                for k in range(1, arr.size):
                    val = arr[k]
                    self.anc['r'] = -1
                    self.anc['mediumaquamarine'].append(start+k)
                    self.ca += 2
                    self.cc += 1
                    j = k-1
                    yield
                    while j >= 0 and val < arr[j]:
                        self.ca += 1
                        arr[j+1] = arr[j]
                        self.anc['r'] = start+j
                        j -= 1
                        yield
                    self.ca += 1
                    arr[j+1] = val
                self.anc['g'].extend(self.anc['mediumaquamarine'])
                self.anc['mediumaquamarine'] = -1
                self.anc['r'] = -1
                yield
            else:
                self.horLine = pivot
                yield

                #else split into two subarrays -> smaller/greater than pivot
                org = organize(start, end, pivot)
                border = -1
                while type(border) != tuple:
                    border = next(org)
                    yield
                border,lo,hi = border

                #add entries to the tree, for further processing
                if border > start:
                    pivot = (lo / (border-start)) if (border - start) > 10 else (self.data[start]+self.data[border-1]+self.data[start+(border-1-start)//2])*0.333
                    pivotTree.append( (start, border, pivot,) )
                if border < end:
                    pivot = (hi / (end-border)) if (end-border) > 10 else (self.data[border]+self.data[end-1]+self.data[start+(end-1-border)//2])*0.333
                    pivotTree.append( (border, end, pivot,) )
        
        self.horLine = -1
        yield
        self.sorted = True