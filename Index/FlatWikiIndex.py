__author__ = 'Jakub Dutkiewicz'
from Index.IIndex import IIndex
import numpy as np
class FlatWikiIndex(IIndex):
    def __init__(self):
        self.Dictionary = {}
        self.Documents = []
    def createIndex(self, foldername):
        fObject = open(foldername)
        iterator = 0
        print 'Creating dictionary...'
        for l in fObject:
            for w in l.split():
                if not self.Dictionary.__contains__(w):
                    self.Dictionary[w] = iterator
                    iterator +=1
                    if iterator%10000 == 0:
                        print str(iterator) + ' entries'
        lght =  len(self.Dictionary)
        print '... created dictionary with ' + str(lght) + ' entries.'
        print 'Creating index'
        fObject.seek(0)
        for i,l in enumerate(fObject):
            self.Documents.append(np.zeros(lght))
            if i%10000 == 0:
                print str(i) + ' documents'
            for w in l.split():
                self.Documents[i][self.Dictionary[w]] += 1
        print 'Successfully created an index'



index = FlatWikiIndex()
index.createIndex('sample file')