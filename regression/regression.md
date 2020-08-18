# Regression

How do we find and estimate the relationships between multiple variables in a large dataset? **Regression analysis** is a set of statistical methods that can relate a dependent variable with one or more independent variables. A **dependent variable** is the outcome variable we are trying to predict; **independent variables** are the predictor variables we are using in our model. A statistical model has the form:

## Write equation properly
Y = f(X_1, X_2...X_N) 

In a linear model, *f* is a linear combination of the dependent variables: 

f = x0 + c1x1 + c1x2+ ... + cnxn

For a linear model to work, the depdent variable must be continuous and the independent variables must be normally distributed. There's some wiggle room around these assumptions (how close to continuous/normal we are), but linear models will misbehave if the data deviates from them.

We'll look at an example using only one variable (**univariate**) to start.