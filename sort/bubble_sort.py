from .sort_base import BaseSort

class BubbleSort(BaseSort):

    def __init__(self, *argv):
        BaseSort.__init__(self, *argv)
        pass

    def sort(self):
        j = 1
        updated = True
        while updated:
            updated = False

            for i in range(self.N-j):
                if self.cmp(i+1, i):
                    self.swap(i, i+1)
                    updated = True
            j += 1

        self.sorted = True
    
    def sortingStep_gen(self):
        self.anc = dict.fromkeys(self.anc, -1)
        self.anc['g'] = []

        j = 1
        updated = True
        while updated:
            updated = False

            for i in range(self.N-j):
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

        self.sorted = True
        self.anc['g'] = list(range(self.N))
        yield