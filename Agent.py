from State import *
from jaro import jaro_winkler_metric
from Levenshtein import distance
import ngram

NUMBER_TO_LETTER = {
        "2" : ["a","i"],
        # "3" : ["aa"],
        "4" : ["gh"],
        "5" : ["kh"],
        "7" : ["h"],
        "8" : ["h"],
        "9" : ["k","q"],
        "a" : ["e"],
        "e" : ["i","u",""],
        "u" : ["o","y",""],
        "gi" : ["j"],
        "x" : ["ch","ks"]
    }

# LETTER_TO_LETTER = {
#     "a" : ["e","2"],
#     "e" : ["i","u","","ee"],
#     "u" : ["o","yo",""],
#     "i" : ["2"],
#     "q" : ["9","k"],
#     "s" : ["ss"],
#     "g" : ["j"],
#     "w" : ["oi"],
#     "x" : ["ch","ks",""]
#     }

VOWELS = ["a","e","y","u","i","o","h","2","w"]

TO_DEPLICATE = VOWELS + ["s","3","r"]

class Agent:
    def __init__(self,expression,number):
        self.expression = expression
        self.state = State(value=expression,parent=None,action=None)
        self.searchField = [self.state]
        self.values = set()
        self.words = set()
        self.number = number
        # self.levin = levin
        # self.ngram = ngram
        # self.jaro = jaro
        
    def word(self):
        for i in self.searchField:
            if i.explored == False:
                for key in NUMBER_TO_LETTER:
                    for l in NUMBER_TO_LETTER[key]:
                        value = self.applyAction(i.value, key, l)
                        if value != "" and value not in self.values:
                            # print(value)
                            self.searchField.append(State(value=value,parent=i,action=key))
                            self.values.add(i.value)
                            if len(self.searchField) == 100:
                                break
                i.explored = True
                
            
    def vis(self,l,j,n,iter):
        if iter  == 0:
            return
        for i in self.values:
            if ngram.NGram.compare(self.expression,i,N=1) >= n and jaro_winkler_metric(self.expression,i) >= j and distance(self.expression,i) <= l:
                self.words.add(i)
        if len(self.words) < self.number:
            self.vis(l,j-0.05,n-0.05,iter-1)


    def getTarget(self,n):
            lst = []
            if len(self.words) <= n:
                return list(self.words) + ['' for i in range(n-len(self.words))]
            for i in self.words:
                lst.append(i)
                if len(lst) == n:
                    return lst

    
    def applyAction(self,exp,a1,a2):
        if exp != exp.replace(a1,a2,1):
            return exp.replace(a1,a2,1)
        return ""
    
    def getWords(self,l,j,n,iter,number):
        self.word()
        self.vis(l=l,j=j,n=n,iter=iter)
        return self.getTarget(number)

    