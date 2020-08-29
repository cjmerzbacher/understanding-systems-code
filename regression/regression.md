# Regression

How do we find and estimate the relationships between multiple variables in a large dataset? **Regression analysis** is a set of statistical methods that can relate a dependent variable with one or more independent variables. A **dependent variable** is the outcome variable we are trying to predict; **independent variables** are the predictor variables we are using in our model. A statistical model has the form:

## Write equation properly
Y = f(X_1, X_2...X_N) 

In a linear model, *f* is a linear combination of the dependent variables: 

f = x0 + c1x1 + c1x2+ ... + cnxn

For a linear model to work, the depdent variable must be continuous and the independent variables must be normally distributed. There's some wiggle room around these assumptions (how close to continuous/normal we are), but linear models will misbehave if the data deviates from them.

We'll look at an example using only one variable (**univariate** regression) to start. For our dataset, we'll be using a LIDAR tree-sensing dataset from here (LINK). LIDAR measures the distance to a target using laser reflections. This dataset includes standardized observations of trees as well as the observed LIDAR height. We want to predict the actual height of the tree from its other characteristics, including the trunk diameter and crown diameter. To start with, let's see if trunk diameter predicts height.

The dependent variable here is tree height. The first independent variable we will consider is the trunk diameter.

## Insert figure with trees labeling trunk percent
