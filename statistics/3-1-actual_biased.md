[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


resp = nsfg.ReadFemResp()

num_kids = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')
print(num_kids)
biased = BiasPmf(num_kids, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([num_kids, biased])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

a = num_kids.Mean()
b = biased.Mean()
print(a)
print(b)
