import nltk
nltk.download('punkt')
nltk.download('punkt_tab')#removing special symbols and split words
nltk.download('stopwords')#remove common english words
nltk.download('wordnet')#convert non grammatical words to grammatical
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
text="""Machine learning,deep learning and natural language processing are 
popular algoriths in ai concept"""
words=word_tokenize(text)
print(words)
stop_words=set(stopwords.words('english'))
#remove common english words
filtered=[w for w in words if w.lower() not in stop_words]
print(filtered)
#removing punctuations
remove_pun=[w for w in filtered if w not in string.punctuation]
print(remove_pun)

