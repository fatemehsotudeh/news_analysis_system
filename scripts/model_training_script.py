#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import joblib


# In[6]:


def fit_and_score(models, X_train, X_test, y_train, y_test):
    np.random.seed(42)
    
    model_scores={}
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        model_scores[name]=model.score(X_test, y_test)
        
    return model_scores


# In[11]:


def tune_hyperparameters(classifier, X, y, param_dist):
    search = RandomizedSearchCV(
        classifier,
        param_distributions=param_dist,
        n_iter=50,
        cv=5, 
        n_jobs=-1,
        random_state=42
    )
    
    search.fit(X, y)

    best_params = search.best_params_

    return best_params


# In[7]:


def save_model(model, path):
    joblib.dump(model, path)


# In[12]:


def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = joblib.load(model_file)
    return model


# In[ ]:




