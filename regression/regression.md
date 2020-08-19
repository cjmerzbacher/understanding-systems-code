# Regression

How do we find and estimate the relationships between multiple variables in a large dataset? **Regression analysis** is a set of statistical methods that can relate a dependent variable with one or more independent variables. A **dependent variable** is the outcome variable we are trying to predict; **independent variables** are the predictor variables we are using in our model. A statistical model has the form:

## Write equation properly
Y = f(X_1, X_2...X_N) 

In a linear model, *f* is a linear combination of the dependent variables: 

f = x0 + c1x1 + c1x2+ ... + cnxn

For a linear model to work, the depdent variable must be continuous and the independent variables must be normally distributed. There's some wiggle room around these assumptions (how close to continuous/normal we are), but linear models will misbehave if the data deviates from them.

We'll look at an example using only one variable (**univariate** regression) to start. For our dataset, we'll be using the fire and tree mortality (FTM) database from the USDA. This dataset includes standardized observations of trees burned in wildfires from 1981 to 2016. We want to predict how likely it is that a tree will survive a fire based on species, fire size, and other tree-level and fire-level attributes. To start with, let's see if scorching predicts tree survival. 

We want to find a dependent variable that tells us whether or not a tree burned. The yr0status variable is 0 for trees that survived the fire and 1 for trees that did not. We've removed trees that were not assessed in the first year after the fire.

The independent variable we are using in this analysis is the percentage of tree crown volume that was scorched. 

## Insert figure with trees labeling CVS percent
