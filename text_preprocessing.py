import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from flask import Flask, redirect, url_for, request


app = Flask(__name__)  

@app.route('/Process_user_data',methods = ['GET']) 



def processing():
    try:
        text = request.args.get('user_input')
        ps = PorterStemmer()
        lemmatizer = WordNetLemmatizer()
        stop_words = stopwords.words('english')
        clean_text = []
        result = ''
        text = text.lower()

        text = re.sub('[^\w\s]',' ', text)
        text = re.sub('[\d]',' ', text)
        text =' '.join([w for w in text.split() if len(w)>1] )
        words = nltk.word_tokenize(text)

        for word in words:
            if word not in stop_words:
                word = ps.stem(word)
                clean_text.append(lemmatizer.lemmatize(word))
                result = ' '.join(map(str, clean_text))
        return result 
    except:
        return 'an exception occured'


if __name__ == "__main__":
    app.run(debug = True)