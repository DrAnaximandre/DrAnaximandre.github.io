Title:  PCA - not only dimension reduction !
Date: 2015-12-05
Category: Dimension reduction, Data Visualization
Summary: A bit of Principal Component Analysis.



## 1 - First example

Let's try to understand the method on simulated data first. Let us denote $X\sim \mathcal{N}(2,1)$ and $Y\sim 1.5X+\mathcal{N}(1.2,1)$ and have $1000$ points from the join distributions, that will be our dataset.
It is straightforward that the two variables are not independant since $Y$ is basically a coefficient times $X$ plus some noise and $X$ is noise. 
While trying to compute their covariance I go stuck on the distribution of $XY$ ([see  : modified Bessel functions of the second kind](http://mathoverflow.net/questions/11800/what-is-the-probability-distribution-function-for-the-product-of-two-correlated)), but actually you don't really need that to compute the covariance and correlation.
I have put the details in the appendix and found a correlation of $\approx.83$ (or a covariance of $1.5$, same same).

So we plot our data (using seaborn yay).

![Data with correlation](/images/figure_PCA_1.png)

The correlation (on this sample) is 0.82, the marginal distributions are roughly normals (how surprising) and we have a kind of a line (like a trend) between the dots. The director coefficient of that line ... should be $1.5$. Advanced data science. 

Now I'm going to perform a magic trick : the PCA. Let's use [scikit's](http://scikit-learn.org/stable/) implementation. It's basically 1 line of code and no, you don't need to know what a PCA is so far, just observe.

![Same data after the PCA](/images/figure_PCA_2.png)

What the flip ? The marginals are still roughly normals (although the order of magnitude -the values on the axis - changed), but the correlation is super-duper small ($e-16$), consequently the dots look more like a realisation of 2 independants normals (but it's not). Also the dots are red now. 

What happened here ? And why is it useful/cool ? 


## 2 - Theory


### 2.1 - Reminder: the SVD
The PCA is based on the Singular Value Decomposition. Or at least it is a way to see it.

Consider a matrix $X$ of dimension $(n,p)$ (that is $n$ lines and $p$ columns, or from the statistician's point of view, $n$ individuals and $p$ features if $X$ is the sample matrix). Let's assume that n>p for simplicity (the dimensions of the matrix defined further will change if not). 
For whatever reason, we're going to decompose this matrix into $3$ matrices. 


**Statement:** There exists a factorization, written as:
$$X = U \boldsymbol{\Sigma} V'$$

where:

- $U$ is a (n,n), unitary matrix (meaning $UU'=U'U=I$),
- $\boldsymbol{\Sigma}$ is a (n,p) diagonal matrix with non-negative real numbers on the diagonal (that is to say : full of $0$ but on the diagonal)
- $V$ is a  (p,p), unitary matrix.
The diagonal entries, $\sigma_i$, of $\boldsymbol{\Sigma}$ are the *singular values* of $X$. Usually, they are ordered on a decreasing fashion. Note that on the formula above, it is transposed.

This is the SVD of $X$.


**Example:** 


### 2.2 What's beneath the PCA

There are many ways to define the PCA, to me the easiest one is to say : **the PCA is the SVD of the centered sample matrix**. 

So let's define $X_c$ the centered sample matrix (we substract the mean of each column to ... each column). Let's also define $X_c= U \boldsymbol{\Sigma} V'$ the SVD of that matrix.

The graph in red 





## 3 - Applications

### 3.1 - Dimension reduction


### 3.2 - Basic image compression


## 4 -  Caveat : an example where correlation ain't absence of relationship


## 5 - Bonus : what about a PCA of a LHS? 



## 6 - Sources:


- My courses of [statistics](http://wikistat.fr/) by Besse et al (in French)


## A - Appendix :

### A1:  Covariance between 2 normal variables that are not independents

Let us denote $X\sim \mathcal{N}(2,1)$ and $Y\sim 1.5X+\mathcal{N}(1.2,1)$, we want to know $\text{Cov}(X,Y)$.

- By definition : $\text{Cov}(X,Y) = \mathbb{E}(XY)-\mathbb{E}(X)\mathbb{E}(Y)$. The two last expectations are known or easily computable, yet the tough nut to crack is the expectation of $XY$.

- Denoting $Z\sim\mathcal{N}(1.2,1)$ one can write $Y\sim 1.5X+Z$ where $X \perp\!\!\!\perp Z$. Thus $Y\sim \mathcal{N}(4.2,3.25)$.

- $\mathbb{E}(XY)=\mathbb{E}(X(1.5X+Y))=1.5\mathbb{E}(X^2)+\mathbb{E}(XZ)$

- $\mathbb{E}(XZ)=\mathbb{E}(X)\mathbb{E}(Z)=2.4$ because the two rv are independents.

- We still have to compute $\mathbb{E}(X^2)$ and I'm lazy so we'll use Köning's variance formula: $\mathbb{E}(X^2)=\text{Var}(X)+\mathbb{E}(X)^2=1+4=5$.

- Thus $\mathbb{E}(XY)=1.5*5+2.4=9.9$

- It follows that $\text{Cov}(X,Y) =9.9-2*4.2=1.5$. This is not surprising. Or is it ?

- And the  $\text{Corr}(X,Y)=\frac{1.5}{\sqrt{3.25}}\approx 0.83$. 
