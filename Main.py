from jaro import jaro_winkler_metric
import ngram
from Levenshtein import distance
from State import *
from Agent import *
from Traductor import *
from textblob import TextBlob





# agent = Agent(expression = "was3",number=50)
# agent.word()
# agent.vis(l=3,j=0.75,n=0.75,iter=3)
# lst = agent.getWords(l=3,j=0.95,n=0.95,iter=1000,number=20)



traductor = Traductor()
jomla = traductor.traduct("wafin ghbrti 3lina ashbi")