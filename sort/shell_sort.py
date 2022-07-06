from .sort_base import BaseSort

class ShellSort(BaseSort):

    def __init__(self, *argv):
        BaseSort.__init__(self, *argv)
        self.gap = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        pass

    def sort(self):
        gap = list(self.gap)

        if (gap[-1]*2.2) < self.N:
            #additional jump sizes generation
            while (gap[-1]*2.2) < self.N:
                gap.append(gap[-1] * 2.2)
        else:
            #figure out the best starting gap size
            for i in range(len(gap)-1, -1, -1):
                if gap[i] < self.N:
                    gap = gap[:i+1]
                    break
        
        for g in gap[::-1]:
            for k in range(0, ((self.N-1) % g)+1, 1):
                for i in range(k, self.N, g):
                    val = self[i]
                    j = i-g
                    while j >= 0 and val < self[j]:
                        self.cc += 1
                        self.ca += 1
                        self.data[j+g] = self.data[j]
                        j -= g
                    self.cc += 1
                    self.ca += 1
                    self.data[j+g] = val

        self.sorted = True
    
    def sortingStep_gen(self):
        self.anc = dict.fromkeys(self.anc, -1)
        # self.anc['r'] = i

        gap = list(self.gap)

        if (gap[-1]*2.2) < self.N:
            #additional jump sizes generation
            while (gap[-1]*2.2) < self.N:
                gap.append(gap[-1] * 2.2)
        else:
            #figure out the best starting gap size
            for i in range(len(gap)-1, -1, -1):
                if gap[i] < self.N:
                    gap = gap[:i+1]
                    break
        
        for g in gap[::-1]:
            # print(g)
            for k in range(0, ((self.N-1) % g)+1, 1):
                self.anc['orchid'] = [k]
                for i in range(k, self.N, g):
                    val = self[i]
                    j = i-g
                    self.anc['y'] = list(range(k,self.N,g)) if g > 1 else -1
                    self.anc['orchid'].append(i)
                    self.anc['r'] = -1
                    yield

                    while j >= 0 and val < self[j]:
                        self.cc += 1
                        self.ca += 1
                        self.data[j+g] = self.data[j]
                        self.data[j] = val
                        self.anc['r'] = j
                        j -= g
                        yield
                    self.ca += 1
                    self.cc += 1
                    self.data[j+g] = val

        self.anc['g'] = self.anc['orchid']
        self.anc['orchid'] = -1
        yield
        self.sorted = True