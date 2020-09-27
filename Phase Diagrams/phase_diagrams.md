# Stability Analysis Part 1: Phase Diagram Basics

What do you do when you encounter systems whose dynamics are so complex that the differential equations used to model them can't be (easily) solved with analytical methods? In this section, we explore how phase diagrams can be used to predict the system's future, and to form a qualitative overview of possible state trajectories. We'll apply this method to a fictional stock of "redfish" in a contained environment.

## The Logistic Model

When approaching a system of differential equations, our goal is almost always to be able to predict the system's behavior given any set of initial conditions. We often approach this problem by deducing an algebraic equation we use to calculate precise values over time. But when the differential equations are too complex to solve, as is often the case for ecological applications, we still have options.

Let's demonstrate.

You might be familiar with the **logistic** model for population growth. It uses the following parameters:

* $r$, the population's **intrinsic growth rate**. It's important to differentiate between the intrinsic growth rate and the instantaneous growth rate. $r$ doesn't measure the population's rate of growth at a given time, it dictates the overall speed at which the population approaches
* $K$, the environment's **carrying capacity**. The logistic model assumes that the environment's resources are limited, such that there exists a maximum population size that can be sustained. $K$ represents that maximum size.

(Quick review of the difference between **variables** and **parameters**. Where variables are metrics by which we measure a system's behavior over time, parameters represent conditions that control the path of the system's bhavior. Where variables can be expected to change over time, parameters are generally only changed by influence from outside the system. When we make graphs of system behavior, we'll usually choose a few variables as the graph's axes, whereas parameters will determine the graph's shape.)

Now, the logistic model is actually simple enough to have a reasonable algebraic equation:

$$n=\frac{K}{1+Ae^{-rt}}$$ (1)

in which $n =$ the stock size, $t =$ time, and $A = \frac{K-n_{0}}{n_{0}}$ where $n_{0} =$ the population at $t=0$.

With this equation, we can plot a time series to see the logistic curve:

### Graph 1: Logistic Curve
Stock over time. Sliders for $K$, $r$, and $n_{0}$

From low values of $n_{0}$, the stock grows exponentially: the growing number of fish means the absolute birth rate increases. The growth levels off as resources grow thin and the death rate increases, until the death rate comes to equal the birth rate as the stock approaches its carrying capacity and the system approaches dynamic equilibrium. From values of $n_{0}>K$, we see the opposite. The stock dies off: the limited resources mean the fish experience a higher death rate than birth rate until enough have died that the rates approach equilibrium.

Now we'll demonstrate how the graphical method can be used to make the same predictions.

## The Logistic Model redux

The logistic equation can be written in differential form as

$$\dot{n}=rn\cdot(1-n/K)$$ (2)

in which $\dot{n}=dn/dt$ (analogous to the instantaneous growth rate mentioned above). You can plug in Eqn 1 to verify that it's a solution to Eqn 2. You can also see how $\dot{n}$ decreases as $n$ approaches $K$ and the negative parenthetical term approaches $1$, matching the behavior we saw in the previous section.

We can represent this graphically by plotting the relationship between $\dot{n}$ and $n$.

### Graph 2: First order phase portrait
Growth over stock. Sliders for $r$ and $K$. Vectors and fixed points on the axis.

This is a **phase portrait**. You may remember **phase space** as the space in which all of a system's possible states can be represented. Since Eqn 2 is a first order equation, and the growth rate is uniquely determined by the stock size, the complete phase space is effectively just the $n$-axis. We predict how the system will move through possible states using **trajectories**, which are represented here as vectors on the $n$-axis. We deduce the magnitude and direction of the trajectories by the value of the $\dot{n}$ curve at any given value of $n$.

Notice that the trajectories will only switch directions at points where the $\dot{n}$ curve crosses the $n$-axis. These are the points at which the stock achieves equilibrium. The qualitative structure of the system's trajectories (and therefore its behavior) is dictated by the location and nature of these **fixed points**, which we study using **stability analysis**.

The goal of of stability analysis is to distinguish between fixed points that *attract* the system (**stable points**) and those that *repel* it (**unstable points**). As an example to illustrate the distinction, you might imagine a ball on a curved surface. Unstable points would be those where the ball is perched on a hilltop. Arbitrarily small perturbations send it tumbling away. Stable points would be those where the ball rests in the crook of a valley. Perturbations that might take the ball over the lip of the valley represent a threshold: after any disturbances smaller than the threshold, the ball will return to its position at the bottom.

Returning to our logistic model, we can see from Graph 2 that there are two fixed points, at $n=0$ ($n_{0}$) and $n=K$ ($n_{K}$). We know that small stocks will make use of the abundance of available resources to grow exponentially. On the phase portrait, we see this behavior in the increasingly positive value of $\dot{n}$ for values close to $n_{0}$, which carry the system away from the fixed point. $n_{0}$ is unstable. We also know intuitively that the stock size tends to approach the carrying capacity, which marks $n_{K}$ as a stable point. On the phase portrait, we see that the stock follows positive trajectories for $n<n_{K}$ and negative trajectories for $n>n_{K}$. For all values of $n>0$, the system will be pushed towards the equilibrium at $n=K$. Our intuitive knowledge is corroborated by the math.

(Part of the logistic model's wonderful simplicity is its choice to ignore that very small stocks are more likely to die off than to achieve exponential growth. Fish live in large environments, and at small enough numbers, they might not even be able to find each other often enough to offset their death rate. More complex models correct for this by introducing a **Minimum Viable Population**, a value marking the lowest stock size from which growth can be sustained. These models put the lower fixed point at $n=$ MVP rather than at $n=0$. For $n<$ MVP, $\dot{n}$ will be negative, and the stock will plummet toward a stable point at $n=0$. You might sketch out a phase portrait for such a model as an exercise.)

Generally, for first-order systems, stable fixed points occur when $d\dot{n}/dn$ is negative at an equilibrium point, and unstable fixed points occur when $d\dot{n}/dn$ is positive. What do you think will happen when $d\dot{n}/dn=0$?

## Recap

Phase portraits are useful because they contain information about every possible trajectory or set of initial conditions. We'd need to plot a time series for every qualitatively distinct trajectory to get that amount of information using analytical methods. And when analytical methods aren't available, the graphical method allows us to identify what those qualitative trajectories will look like.

The trade off is that the graphical method does not enable us to easily make quantitative predictions, where a time series can tell us the stock size at any time $t$. The breadth of general information comes at the cost of more specific information. One should choose their approach carefully to match the nature of the problem.
