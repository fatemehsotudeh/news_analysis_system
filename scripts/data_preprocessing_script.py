#!/usr/bin/env python
# coding: utf-8

# In[32]:


from hazm import Normalizer, word_tokenize, stopwords_list, Stemmer, Lemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


# In[33]:


def preprocess_persian_text(text):
    normalizer = Normalizer()
    text = normalizer.normalize(text)

    words = word_tokenize(text)

    words = [word for word in words if word.isalnum()]

    stop_words = set(stopwords_list())
    words = [word for word in words if word not in stop_words]

    lemmatizer = Lemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    processed_text = ' '.join(words)

    return processed_text


# In[34]:


def tf_idf_vectorization(text):
    tfidf_vectorizer = TfidfVectorizer(max_features=1000)  
    text_features = tfidf_vectorizer.fit_transform(text).toarray()
    return text_features




# In[ ]:




