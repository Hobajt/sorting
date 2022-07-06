from .sort_base import BaseSort

class SortTemplate(BaseSort):
    '''Basic structure for the derived Sort classes (bcs I'm that lazy)'''

    def __init__(self, *argv):
        BaseSort.__init__(self, *argv)
        pass

    def sort(self):
        self.sorted = True
    
    def sortingStep_gen(self):
        # self.anc = dict.fromkeys(self.anc, -1)
        # self.anc['r'] = i
        yield
        self.sorted = True