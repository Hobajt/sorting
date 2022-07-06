from .sort_base import BaseSort

class InsertionSort(BaseSort):

    def __init__(self, *argv):
        BaseSort.__init__(self, *argv)
        pass

    def sort(self):
        for i in range(1,self.N):
            j = i-1
            val = self[i]
            while (j >= 0) and self.cmp2(val, j):
                self.data[j+1] = self.data[j]
                self.ca += 1
                j -= 1
            self.data[j+1] = val
            self.ca += 1
        self.sorted = True
    
    def sortingStep_gen(self):
        self.anc = dict.fromkeys(self.anc, -1)  #unset all highlights 
        self.anc['mediumaquamarine'] = [0]
        for i in range(1,self.N):
            j = i-1
            val = self[i]
            self.anc['r'] = -1
            self.anc['mediumaquamarine'].append(i)
            yield
            while (j >= 0) and self.cmp2(val, j):
                self.data[j+1] = self.data[j]
                self.ca += 1
                self.data[j] = val
                self.anc['r'] = j
                j -= 1
                yield
            self.data[j+1] = val
            self.ca += 1
        self.anc['g'] = self.anc['mediumaquamarine']
        self.sorted = True
        yield
