from django.shortcuts import render
from .models import Fake_NEWS
from .models import Authenticate_NEWS
# Create your views here.


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string
import bangla
from langdetect import detect

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


df_fake = pd.read_csv('dataset/LabeledFake-1K.csv')
df_true = pd.read_csv('dataset/LabeledAuthentic-7K.csv')

df_fake = df_fake.sample(frac = 1)
df_true = df_true.sample(frac = 1)


df_fake = df_fake.drop(['F-type'], axis = 1)
df_marge = pd.concat([df_fake, df_true], axis =0 )

df = df_marge.drop(["articleID", "domain","date","category","source" ,"headline","relation"], axis = 1)

df.reset_index(inplace = True)
df.drop(["index"], axis = 1, inplace = True)


# Creating a function to convert the text in lowercase, remove the extra space, special chr., ulr and links.
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

df["content"] = df["content"].apply(wordopt)

x = df["content"]
y = df["label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05)


vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)


# train model
LR = LogisticRegression()
LR.fit(xv_train,y_train)

DT = DecisionTreeClassifier()
DT.fit(xv_train, y_train)


forest = RandomForestClassifier(n_estimators=1000 )
forest.fit(xv_train,y_train)  


def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"
    
def manual_testing(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt) 
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)

    pred_LR = LR.predict(new_xv_test)
    
    pred_DT = DT.predict(new_xv_test)

    pred_rm = forest.predict(new_xv_test)

    value = 1

    if pred_rm == 0  or pred_LR == 0 or pred_DT == 0:
        value = 0
    else:
        value = 1

    # return pred_rm
    # return pred_DT
    # return pred_LR
    return value


# Create your views here.
def actionFakeNews(request):
    if request.method == 'POST':


        # forest = RandomForestClassifier(n_estimators=1000 )
        # forest.fit(xv_train,y_train)  

        # sentence = "'দেশের রাজনীতি দিনকে দিন পচে যাচ্ছে।'"
        
        data ={'c' : request.POST.get('url')}

        news = data['c']

        def remove(string):
                return string.replace("  ", "")
            
        text = str(remove(news))

        InputType = news.isnumeric()
        
        if InputType == False:
            ds = detect(text)

            if ds == 'bn' :
                label =  manual_testing(text)
                if label == 0:
                    data={'a' : "Fake News",'b' : news}
                else:
                    data={'aa' : "Not A Fake News",'b' : news}
            else:
                data={'z' : 'We accept only bangla NEWS' ,'b' : news}
        else:
            data={'z' : 'Number Can not be NEWS' ,'b' : news}
    else:
        data = {'d' : 'No Request Found'}
    return render(request,'index.html',data)