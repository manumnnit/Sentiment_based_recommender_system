Title: Sentiment based recommender System (Capstone Project)
Developed by: Mandheer Singh
Deployed At: https://sentiment-based-reco-sys.herokuapp.com

Date: 11/04/2021

Description: We will be using the e-commerce product reviews data set to build a product recommendation system for the end users. The recommendations will be improved using a sentiment analysis model. Thus, you we know that reviews and ratings help you in buying the product.

    You know that, as a user, you need to manually look into the reviews and ratings to make decisions on whether to buy a product or not. But, at the same time, you notice that when you access the website or the Android application of e-commerce websites such as Amazon and Myntra, you get the recommendations of the products that are quite similar to your preferences. We are trying to automate this manual processes by recommending products to the user.

    These recommendations can be improved by analysing the sentiments on the reviews of the recommended products. In order to do this, we need two models: A recommendation system and a sentiment analysis model.

Let's start with the sentiment analysis model. Based on the product reviews, we build a machine learning model that can give the corresponding sentiments of each of the products present in the data (Positive or Negative). Following steps are used:
        
        1. Data cleaning

        3. Text preprocessing ( tokenisation, punctuation and stopwords removal, noise removal, stemming)

         4. Feature extraction or feature creation using TF-IDF vectorizer

        5. Training of text classification models for sentiment analysis using the ML techniques such as logistic regression, random forest, XGBoost and Naive Bayes algorithm. Finally we choose Logistic regression model with oversampling of the negative class

        6. Evaluation and comparing the results of multiple ML models built and choosing the one. Finally we choose Logistic regression model with oversampling of the negative class

Next part is to build a recommender system We used these two approaches:
    1. User- based filtering
    2. Item-based filtering
    We choose User-based filtering as it performed better

How to run this Project:
 1. Go to the URL: https://sentiment-based-reco-sys.herokuapp.com
 2. Provide the User Name Top 5 recommendation will then be displayed on the app sorted by their positive reviews percentage(User must be present in the dataframe)
    (Try Username - joshua)

 Tools Used:
 1. Models have been trained and pickeled using google colab
 2. Web app is made using Flask and Python
 3. Deployed on Heroku using Github

 Requirements:
  Refer requirements.txt for details



 