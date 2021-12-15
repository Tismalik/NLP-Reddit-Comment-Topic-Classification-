<h1 allign:'center'> NLP Reddit Comment-Topic Sentiment Classification </h1>
<h3> Objective: Sentiment Analysis and classification of reddit comment using topic for analysis context </h3> 
<p>
Data set was generated using Pushshift API, some preprocessing measure were taken, NLTK toolkit VADER was then initiated to generate base polarity score.
  A measure was enacted to determine polarity type and a logic was developed to generate final label/score.
  A word2vec model was trained using the word in the data, its features were solely used in the training and testing process. BOW & td-idf features were also generated purely for learning purposes.
  Several ML Classification algortihms were then applied to the data to build a model.
  The selected model was a MLP Neural Network with hidden layer(2,3)
</p>
```

Classification Report
╔═══════════╦════════════════════╗
║   Scores  ║                    ║
╠═══════════╬════════════════════╣
║ accuracy  ║ 0.999999           ║
║ precision ║ 0.999999           ║
║ recall    ║ 0.999999           ║
║ F1        ║ 0.999999           ║
╚═══════════╩════════════════════╝

```
