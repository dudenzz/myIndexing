__author__ = 'Jakub Dutkiewicz'
import numpy as np
class FlatWikiIndex():
    def __init__(self):
        self.Dictionary = {}
        self.Documents = []
        self.Frequencies = {}
    def createIndex(self, foldername):
        fObject = open(foldername)
        iterator = 0
        iterator2 = 0
        print 'Creating dictionary...'
        for l in fObject:
            for w in l.split():
                if not self.Frequencies.__contains__(w):
                    self.Frequencies[w] = 0
                    iterator +=1
                    if iterator%10000 == 0:
                        print str(iterator) + ' parsed words (2016 wiki contains 8392514 words)'
                else:
                    self.Frequencies[w] += 1
                    if self.Frequencies[w] == 5:
                        self.Dictionary[w] = iterator2
                        iterator2 +=1
                        if iterator2%10000 == 0:
                            print str(iterator2) + ' entries'

        lght =  len(self.Dictionary)
        print '... created dictionary with ' + str(lght) + ' entries.'
        print 'Creating index'
        fObject.seek(0)
        for i,l in enumerate(fObject):
            self.Documents.append({})
            if i%10000 == 0:
                print str(i) + ' documents'
            for w in l.split():
                if self.Dictionary.__contains__(w):
                    if not self.Documents[i].contains(self.Dictionary[w]):
                        self.Documents[i][self.Dictionary[w]] = 1
                    else:
                        self.Documents[i][self.Dictionary[w]] += 1
        print 'Successfully created an index'

    def saveIndex(self, filename):
        fObject = (filename)


index = FlatWikiIndex()
index.createIndex('sample file')