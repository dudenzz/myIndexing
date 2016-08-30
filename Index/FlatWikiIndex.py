__author__ = 'Jakub Dutkiewicz'
import numpy as np
class FlatWikiIndex():
    def __init__(self):
        self.Dictionary = {}
        self.Documents = []
        self.Frequencies = {}
        self.InverseIndex = {}
    def createIndex(self, foldername):
        fObject = open(foldername)
        iterator = 0
        iterator2 = 0
        print 'Creating dictionary...'
        for l in fObject:
            for w in l.split():
                if not self.Frequencies.__contains__(w):
                    self.Frequencies[w] = 1
                    iterator +=1
                    if iterator%100000 == 0:
                        print str(iterator) + ' parsed words (2016 wiki contains 8392514 words)'
                else:
                    self.Frequencies[w] += 1
                    if self.Frequencies[w] == 5:
                        self.Dictionary[w] = iterator2
                        self.InverseIndex[iterator2] = []
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
                print str(i) + ' documents (wiki 2016 = 3977901 documents)'
            for w in l.split():
                if self.Dictionary.__contains__(w):
                    if not self.InverseIndex[self.Dictionary[w]].__contains__(i):
                        self.InverseIndex[self.Dictionary[w]].append(i)
                    if not self.Documents[i].__contains__(self.Dictionary[w]):
                        self.Documents[i][self.Dictionary[w]] = 1
                    else:
                        self.Documents[i][self.Dictionary[w]] += 1
        print 'Successfully created an index'

    def saveIndex(self, fDObject, fFObject, fIndObject, fInvIndObject):
        for w in self.Dictionary:
            fDObject.write(str(w) + ' ' + str(self.Dictionary[w]) + '\n')
        for f in self.Frequencies:
            fFObject.write(str(f) + ' ' + str(self.Frequencies[f]) + '\n')
        for file in self.Documents:
            fIndObject.write(str(file) + '\n')
        for word in self.InverseIndex:
            fInvIndObject.write('{' + str(word) +': ' + str(self.InverseIndex[word]) + '}' + '\n')

index = FlatWikiIndex()
index.createIndex('sample file')
print index.Documents
print index.Dictionary
print index.Frequencies
print index.InverseIndex

fdo = open('dict','w+')
ffo = open('freq','w+')
fio = open('index','w+')
fiio = open('inverse','w+')
index.saveIndex(fdo,ffo,fio,fiio)