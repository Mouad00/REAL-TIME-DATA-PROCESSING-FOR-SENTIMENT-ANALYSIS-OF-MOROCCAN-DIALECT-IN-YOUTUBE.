
class Traductor:
    def __init__(self):
        self.url = './dataset/data.csv'
       
    def traduct(self,sentence):
        out = ""
        file = open(self.url, 'r')
        lines = file.readlines()
        for line in lines:
            lst = line.split(',')
            for word in lst:
                if word in sentence and word != '':
                    # sentence.replace(word,lst[-1])
                    print(word)
                    out += lst[-1]
                    
        return ' '.join(dict.fromkeys(out.split()))
            