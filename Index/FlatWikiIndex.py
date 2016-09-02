__author__ = 'Jakub Dutkiewicz'
import numpy as np
import threading

class indexingThread(threading.Thread):
    def __init__(self, threadID, name, dictionary, texts):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.InverseIndex = {}
        self.Documents = []
        self.Texts = texts
        self.Dictionary = dictionary
    def run(self):
        print "Starting " + self.name
        for w in self.Dictionary:
                self.InverseIndex[self.Dictionary[w]] = []
        for i,l in enumerate(self.Texts):
            self.Documents.append({})
            if i%10000 == 0:
                print str(i) + self.name + ' documents (wiki 2016 = 397790 documents per thread)'
            for w in l.split():
                if self.Dictionary.__contains__(w):
                    if not self.InverseIndex[self.Dictionary[w]].__contains__(i):
                        self.InverseIndex[self.Dictionary[w]].append(i)
                    if not self.Documents[i].__contains__(self.Dictionary[w]):
                        self.Documents[i][self.Dictionary[w]] = 1
                    else:
                        self.Documents[i][self.Dictionary[w]] += 1
        print "Exiting " + self.name

class FlatWikiIndex():
    def __init__(self):
        self.Dictionary = {}
        self.InverseIndex = {}
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
        print 'Creating document identifiers...'
        docs = []
        fObject.seek(0)
        for i,j in enumerate(fObject):
            if i%10000 == 0:
                print str(i) + ' document ids assigned (wiki 2016 = 3977901 documents)'
            docs.append(j)

        print 'Creating 10 workers'
        self.worker1 = indexingThread(1, 'Thread-1', self.Dictionary, docs[0:400000])
        self.worker2 = indexingThread(2, 'Thread-2', self.Dictionary, docs[400000:800000])
        self.worker3 = indexingThread(3, 'Thread-3', self.Dictionary, docs[800000:1200000])
        self.worker4 = indexingThread(4, 'Thread-4', self.Dictionary, docs[1200000:1600000])
        self.worker5 = indexingThread(5, 'Thread-5', self.Dictionary, docs[1600000:2000000])
        self.worker6 = indexingThread(6, 'Thread-6', self.Dictionary, docs[2000000:2400000])
        self.worker7 = indexingThread(7, 'Thread-7', self.Dictionary, docs[2400000:2800000])
        self.worker8 = indexingThread(8, 'Thread-8', self.Dictionary, docs[2800000:3200000])
        self.worker9 = indexingThread(9, 'Thread-9', self.Dictionary, docs[3200000:3600000])
        self.worker10 = indexingThread(10, 'Thread-10', self.Dictionary, docs[3600000:])
        print 'Running threads'
        self.worker1.start()
        self.worker2.start()
        self.worker3.start()
        self.worker4.start()
        self.worker5.start()
        self.worker6.start()
        self.worker7.start()
        self.worker8.start()
        self.worker9.start()
        self.worker10.start()
        self.worker1.join()
        self.worker2.join()
        self.worker3.join()
        self.worker4.join()
        self.worker5.join()
        self.worker6.join()
        self.worker7.join()
        self.worker8.join()
        self.worker9.join()
        self.worker10.join()
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
    def readIndex(self, fDObject, fFObject, fIndObject, fInvIndObject):
        for w in fDObject:
            self.Dictionary[w.split()[0]] = int(w.split()[1])
        for w in fFObject:
            self.Frequencies[w.split()[0]] = int(w.split()[1])


c = FlatWikiIndex()
c.createIndex('sample file')

print c.worker1.InverseIndex