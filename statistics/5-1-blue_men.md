[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

mu = 178
sigma = 7.0
dist = sp.stats.norm(loc=mu, scale=sigma)
outside = dist.cdf(mu-sigma)
print(outside)

low = dist.cdf(177.8)
high = dist.cdf(185.4)
print(low, high, high-low)
