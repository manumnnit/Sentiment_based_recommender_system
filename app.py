
from flask import Flask, request, render_template
import pandas as pd
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle

# Loading all necessary resources and models
f1=open('./models/reviews.pkl','rb')
reviews=pickle.load(f1)
f2=open('./models/vect.pkl','rb')
vect=pickle.load(f2)
f3=open('./models/lr2.pkl','rb')
lr2=pickle.load(f3)
f4=open('./models/user_final_rating.pkl','rb')
user_final_rating=pickle.load(f4)

# Function which takes item id as input and return % of postive reviews
def reviews_sentiment(item_id):
  item_reviews=reviews.loc[reviews['id']==item_id,'review']
  item_features=vect.transform(item_reviews)
  sentiment=lr2.predict(item_features)
  sentiment=[1 if x=='Positive' else 0 for x in sentiment]
  pos_reviews=sum(sentiment)
  pos_reviews_percent=100*pos_reviews/len(sentiment)
  return pos_reviews_percent



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommend',methods=['POST'])
def recommend():
    if (request.method == 'POST'):
        user=request.form['UserName']
        if user in user_final_rating.index:
            g=user_final_rating.loc[user].sort_values(ascending=False)[:20] #top 20 items
            f=pd.DataFrame(g.index)
            f['pos_review_per']=f['id'].apply(reviews_sentiment) #fine tuning by using sentiment analyzer
            final=pd.DataFrame(f.sort_values(by=['pos_review_per'],ascending=False)[:5]) #filtering top 5 recommendations
            merged=pd.merge(final,reviews,how='left',left_on='id',right_on='id')
            merged=merged[['id','brand','name','pos_review_per']]
            final_items=merged.drop_duplicates(keep='first')
            return render_template('index.html',tables=[final_items.to_html(classes='data', header=True,index=False)])
        else:
            return render_template('index.html',user_not_found='User Not found in database')


if __name__ == '__main__':
    app.run(debug=True)
