#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.tokenize import word_tokenize
from math import *
import sys


# In[3]:


def extractWords(aline):
    rawSentence = word_tokenize(aline)
    sentence = []
    for token in rawSentence:
        if token not in ".,?!;:-(){}[]'\"":
            sentence.append(token)
    return sentence



def trainNaiveBayes(fileList):
    V = []
    D = {"0":[], "1":[]}
    likelihood = {}
    countPos = 0
    countNeg = 0
    docCount = 0
    for afile in fileList:
        file = open(afile, "r")
        for line in file:
            sentence = extractWords(line)
            if len(sentence) == 0:
                pass
            else:
                docCount += 1
                sentiment = sentence.pop(-1)
                if sentiment == "0":
                    countNeg += 1
                elif sentiment == "1":
                    countPos += 1
                for word in sentence:
                    if word not in V:
                        V.append(word.lower())
                    D[sentiment].append(word.lower())
    #Calculating P(c) terms
    probNeg = log(countNeg/docCount)
    probPos = log(countNeg/docCount)
    
    #Calculating P(w|c) terms
    for word in V:
        likelihood[word] = []
        numNeg = D["0"].count(word)
        likelihood[word].append(log((numNeg+1)/(countNeg+len(V))))
        
        numPos = D["1"].count(word)
        likelihood[word].append(log((numPos+1)/(countPos+len(V))))
    
    return D, V, likelihood, probNeg, probPos





def testNaiveBayes(doc, V, likelihood, probNeg, probPos):
    testDoc = open(doc, "r")
    resultFile = open("results_file.txt", "w")
    for line in testDoc:
        tokens = extractWords(line.lower())
        psum = [probNeg, probPos]
        for word in tokens:
            if word in V:
                pGivNeg = likelihood[word][0]
                pGivPos = likelihood[word][1]
                psum[0] += pGivNeg
                psum[1] += pGivPos
        if psum[0] > psum[1]:
            finalSent = "0"
        else:
            finalSent = "1"
        resultFile.write(finalSent+"\n")
    testDoc.close()
    resultFile.close()
    
  


        
testResults = trainNaiveBayes(["sentiment/amazon_cells_labelled.txt", "sentiment/imdb_labelled.txt", "sentiment/yelp_labelled.txt"])
testNaiveBayes(sys.argv[1], testResults[1], testResults[2], testResults[3], testResults[4])


