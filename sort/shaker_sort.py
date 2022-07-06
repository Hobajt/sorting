from .sort_base import BaseSort

class ShakerSort(BaseSort):

    def __init__(self, *argv):
        BaseSort.__init__(self, *argv)
        pass

    def sort(self):
        updated = True
        j = 1
        k = 0
        while updated:
            updated = False

            for i in range(k, self.N-j):
                if self.cmp(i+1, i):        #if data[i] > data[j]
                    self.swap(i, i+1)
                    updated = True
            j += 1

            if not updated:
                break

            for i in range(self.N-j, k-1, -1):
                if self.cmp(i+1, i):
                    self.swap(i, i+1)
                    updated = True
            k += 1

        self.sorted = True
    
    def sortingStep_gen(self):
        self.anc = dict.fromkeys(self.anc, -1)
        self.anc['g'] = []

        j = 1
        k = 0
        updated = True
        while updated:
            updated = False

            for i in range(k, self.N-j, 1):
                self.anc['y'] = [i, i+1]
                self.anc['r'] = -1
                yield
                if self.cmp(i+1, i):
                    self.swap(i, i+1)
                    updated = True
                    self.anc['r'] = self.anc['y']
                yield
            self.anc['g'].append(self.N-j)
            j += 1
            yield

            if not updated:
                break

            for i in range(self.N-j, k-1, -1):
                self.anc['y'] = [i, i+1]
                self.anc['r'] = -1
                yield
                if self.cmp(i+1, i):
                    self.swap(i, i+1)
                    updated = True
                    self.anc['r'] = self.anc['y']
                yield
            self.anc['g'].append(k)
            k += 1
            yield
        self.anc['g'] = list(range(0, self.N, 1))
        self.sorted = True
        yield