# Clustering Graphs

What happens if we have data on the features of a particular object set, but not information on how or how much those objects interact? How do we hypothesize functional similarity or interaction?

One common example of datasets of this type is **gene expression data**. We can obtain the relative amount a gene is expressed under different conditions using microarray hybridization experiments. We would expect genes with similar functions to be similarly expressed. Thus, if we cluster the features of the dataset, we may find modules of genes with mechanistic connections.

The sample dataset used in this section is yeast mitotic cell cycle data (Cho, 1998). A sample of the dataset is below. There are columns for the gene name (if known) and its relative expression levels at timepoints 0 to 160 minutes.

## Insert head of datatable here

Often, experimental data must be preprocessed to remove noise, outliers, and normalize the features of interest. In this case, we remove the 10th and 11th time points as outliers and remove genes with low average activity and low variability as not relevant to the environmental conditions of interest. We also normalize the gene expression vectors to have an average of 0 and a standard deviation of 1.

## Normalization figure here

There are a variety of clustering algorithms, but all of them rely on calculating how close individual data points are to each other. But what does distance mean in a high-dimensional space like our gene expression data? One common distance metric is the **Euclidean distance**. The euclidean distance between two points is defined as 
 
 ## Euclidean distance equation

The most common method of clustering a graph is **k-means clustering**. K-means clustering requires the user to input the number of clusters expected, or k, as a parameter. Initially, k centroids are randomly created.

## Initial randomly distributed centroids

Each data point is assigned to the cluster of the closest centroid (using Euclidean distance). The sample assignment function is below.

## Insert assignment code

## Figure displaying original centroid positions

Now, the centroids of the assigned clusters are recalculated. 

## Update code

## Figure displaying new centroid positions with arrows

This process - assign data to clusters, then update the cluster centroids - is repeated until the centroids no longer change location significantly.

## Iteration code 

## Figure displaying final clustering results

Often, however, we do not initially know how many clusters exist in our data. We can run the k-means clustering algorithm for a variety of k values and plot the average distance to the centroid of the cluster. This plot is known as an **elbow plot**. 

## Insert elbow plot here

Similar clustering methods to k-means use other metrics of centrality to determine centroid location (for example, the medoid) or use similarity measures rather than strict classification. 

Another class of methods is agglomerative clustering methods. These methods start with all data points in separate clusters and merge close clusters iteratively until all points are combined in a single cluster. 

## Insert code for AC

## Insert AC clustering diagram

Agglomerative methods do not assume an exact number of clusters. Instead, the results are displayed as a **dendrogram** and the analyst can select the appropriate number of agglomerative iterations to reach an optimal number of clusters.

## Insert dendrogram here

Applying these two methods to our yeast gene expression data set, we can see ...

## Add results of analysis here



Note: All 2D visualizations here are of higher-dimensional data reduced using linear discriminant analysis (LDA).

Hierarchical clustering (Agglomerative) 
Select: single linkage, complete li


- [ ] Include Pearson correlation, not just Euclidean distance
- [x] Project clusters into 2D with LDA(?)
    https://towardsdatascience.com/dimensionality-reduction-toolbox-in-python-9a18995927cd
- [ ] Animation of clustering over time
- [ ] Elbow plot of different k
    - [ ] Calculate distortion https://www.geeksforgeeks.org/elbow-method-for-optimal-value-of-k-in-kmeans/
- [ ] Agglomerative clustering
- [ ] Add results of analysis
- [ ] draw simple diagrams for clustering methods
- [ ] Normalization figure
- [ ] Display data table 
- [ ] Euclidean distance location
- [ ] insert code