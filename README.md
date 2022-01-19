<h1 allign:'center'> NLP Reddit Comment-Topic Sentiment Classification </h1>
<h3> Objective: Sentiment Analysis and classification of reddit comment using topic for analysis context </h3> 
<body>
<p>The Data set was generated using Pushshift API, some Preprocessing measure were taken, NLTK toolkit VADER was then initiated to generate base polarity score.</p>
<p> A measure was enacted to determine polarity type and a logic was developed to generate final label/score. </p>
<p> A word2vec model was trained using the word in the data, its features were solely used in the training and testing process. BOW & td-idf features were also generated purely for learning purposes. </p>
<p> Several ML Classification algortihms were then applied to the data to build a model. </p>
<p>The selected model was the Random Forrest Classifier with a 87% Accuracy </p>


```
Classification Report::
              precision    recall  f1-score   support

         neg       0.86      0.82      0.84      1632
         neu       1.00      1.00      1.00       673
         pos       0.85      0.88      0.86      1840

    accuracy                           0.88      4145
   macro avg       0.90      0.90      0.90      4145
weighted avg       0.88      0.88      0.88      4145
```
<body style="background-color:white;">
    <h1>Confusion Matrix </h1>
    <img src="https://user-images.githubusercontent.com/78315034/150137255-6950a2c0-049d-4bc2-9a3b-f8114e98c58f.png">
</body>

<body style="background-color:white;">
    <h1>ROC Curve </h1>
    <img src="https://user-images.githubusercontent.com/78315034/150137646-ae7dfd18-0d35-497b-9f23-b2a0c04efa16.png">
</body>
