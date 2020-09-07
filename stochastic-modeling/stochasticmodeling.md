# Stochastic Modeling

One of the important assumptions of the differential equation models considered previously is a continuous distribution of the proteins or molecules of interest. In reality, cells contain only a finite (and usually quite small) number of a particular molecule. In some cases, we do not care to model individual cells: we may be able to consider a population of cells as a single unit, for instance in the case of a bulk bioreactor. However, for other applications we may want to examine gene expression in individual cells. Single-cell analysis is a growing family of techniques that allows scientists to study heterogeneous populations of cells and understand complex intercellular dynamics. 

## Gif of glowing proteins in cell cycle

To more adequately describe these **low-copy number dynamics**, we will use stochastic modeling. The system is quite similar to the one considered in the differential equations section [LINK]:

### Figure (mRNA, protein gene)

However, instead of using deterministic equations, we will model the probability of making a protein or mRNA molecule. The number of mRNA per cell cycle is distributed in a Poisson distribution, like many biological phenomena: 

## Poisson equation

A Poisson distribution is a distribution that models the number of events occuring within a given time interval (in this case, the length of a single cell cycle). $\lambda$ is the shape parameter, which indicates the average number of events in the time interval.

The mean number of proteins, on the other hand, is dependent on the number of mRNA molecules. For each time step, the mRNA molecule can either degrade or replicate into a protein:

## Figure with mRNA replicating, degradation loop

Given a probability that an mRNA produces a protein $p$, the probability of producing 0, 1, 2, or N proteins is:

## Prob of producing different proteins equations

This mechanism results in a geometric distribution. Note that the mean number of proteins is actually not the most likely number in the cell.

## Summary figure of poisson, geometric distributions.

