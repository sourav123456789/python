# Its used to get the root word
import nltk
from nltk.data import find
from nltk.stem import WordNetLemmatizer

try:
    find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# Optional: also check for 'omw-1.4'
try:
    find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("congratulations" , pos = 'n'))