# going , gone , -> go ,    eat , eating , eaten -> eat

## we ll use porterStemmer
from nltk.stem import PorterStemmer , RegexpStemmer

words = ["eat" , "eating" , "eaten" , "go" , "going" , "gone" , "final" , "finally" , "history"
         , "congratulations"]

stemming = PorterStemmer()
for word in words:
    print("word is " + word +   " " + "stem is" + " " + stemming.stem(word))

reg_stemmer = RegexpStemmer("ing$|able$|s$|e$" , min = 6)
print(reg_stemmer.stem('eating'))
