# Its used to tokenize a sentence to words.

from nltk.tokenize import sent_tokenize, word_tokenize , wordpunct_tokenize , TreebankWordTokenizer
corpus = """My name is sourav. This is my youtube's channel"""
ans = sent_tokenize(corpus)
ans1 = word_tokenize(corpus)
ans2 = wordpunct_tokenize(corpus)
tokenizer = TreebankWordTokenizer()
ans4 = tokenizer.tokenize(corpus)
print(ans)
print(ans1)
print(ans2)
print(ans4)
