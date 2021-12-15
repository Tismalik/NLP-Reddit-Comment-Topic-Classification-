<h1 allign:'center'> NLP Reddit Comment-Topic Sentiment Classification </h1>
<h3> Objective: Sentiment Analysis and classification of reddit comment using topic for analysis context </h3> 
<body>
<p>The Data set was generated using Pushshift API, some Preprocessing measure were taken, NLTK toolkit VADER was then initiated to generate base polarity score.</p>
<p> A measure was enacted to determine polarity type and a logic was developed to generate final label/score. </p>
<p> A word2vec model was trained using the word in the data, its features were solely used in the training and testing process. BOW & td-idf features were also generated purely for learning purposes. </p>
<p> Several ML Classification algortihms were then applied to the data to build a model. </p>
<p>The selected model was a MLP Neural Network with hidden layer(2,3) </p>
</body>


```
Classification Report::
precision    recall  f1-score   support

         neg       1.00      1.00      1.00       379
         neu       1.00      1.00      1.00       182
         pos       1.00      1.00      1.00       417

    accuracy                           1.00       978
   macro avg       1.00      1.00      1.00       978
weighted avg       1.00      1.00      1.00       978

```
 # Confusion Matrix 
![output](https://user-images.githubusercontent.com/78315034/146198184-95c18a49-8d49-41b0-8f9a-b4fa4b3a3921.png)
