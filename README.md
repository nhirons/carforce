# Predicting service operations from connected car telematics

## Authors
* Nicholas Hirons, Julian Kudszus, Soham Kudtarkar, Spencer Lee
* Data courtesy of [CarForce](http://www.thecarforce.com/)

## Outline
* Predict likely service operations from engine error codes, time of year and car features such as make, age, mileage, engine size, fuel type
* Compared SVMs, random forests, logistic regression and k-NN
* Paramaters tuned using 5-fold cross validation on 75% of data, tested on remaining 25%
* Given output class imbalance, F-score was used as key metric for performance
* k-NN outperformed other algorithms but overall results were mixed
* Strongest results for predicting whether tires need to be inflated (F-score of 67%)

## Live Demo
* See this [notebook](https://github.com/nhirons/carforce/blob/master/1_live_demo.ipynb) for summarized walkthrough of cleaning, preprocessing, model training and inference.