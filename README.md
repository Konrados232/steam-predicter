# Steam Predicter
Machine Learning project focused on predicting whether the Steam game is good or bad based on its categories, tags, price, number of owners, developers and many other things. Project is divided into two parts - one focused on purely analysis and learning process of different models, and the other one focused on using trained model and predicting the output on selected games.

Project is written in Python using Jupyter Notebooks and scikit-learn, tensorflow, numpy, matplotlib libraries.


## Learning Part
* main.ipynb - notebook focused on selecting, cleaning and merging datasets from kaggle.com.
* analysis.ipynb - notebook focused on data analysis and visualization using various plots.
* predict.ipynb - notebook focused on learning different models, varying from Linear SVC or Logistic Regression to neural networks, and comparing their statistics such as accuracy, recall and precision based on sample data.


## Predicting Part
* main.py - is mainly used for fetching data from APIs and transforming them for model to predict.
* APIPredict.ipynb - notebook using fetched data from APIs and best model to predict whether Steam has positive reviews or not.

Other files contain helper classes.
