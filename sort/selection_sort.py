from .sort_base import BaseSort

class SelectionSort(BaseSort):

    def __init__(self, *argv):
        BaseSort.__init__(self, *argv)
        pass

    def sort(self):
        for i in range(self.N):
            idx = i
            val = self[i]
            for j in range(i, self.N):
                self.cc += 1
                if self[j] < val:
                    idx = j
                    val = self.data[j]
            self.data[idx] = self.data[i]
            self.data[i] = val
            self.ca += 2
        self.sorted = True
        pass
    
    def sortingStep_gen(self):
        self.anc = dict.fromkeys(self.anc, -1)
        self.anc['g'] = []
        for i in range(self.N):
            idx = i
            val = self[i]
            self.anc['seagreen'] = self.anc['r'] = -1
            self.anc['g'].append(i)
            self.anc['y'] = i
            yield
            for j in range(i, self.N):
                self.cc += 1
                if self[j] < val:
                    idx = j
                    val = self.data[j]
                    self.anc['seagreen'] = j
                self.anc['r'] = j
                yield
            self.data[idx] = self.data[i]
            self.data[i] = val
            self.ca += 2
            yield
        self.sorted = True